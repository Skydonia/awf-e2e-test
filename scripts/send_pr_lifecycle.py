from __future__ import annotations

import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any

from agentic_workflow.pr_lifecycle import (
    LifecycleTelemetryError,
    build_lifecycle_payload,
    dispatch_repository_event,
    extract_episode_payload,
)


def warning(message: str) -> None:
    print(f"::warning title=AWF lifecycle telemetry::{message}")


def _enabled(value: str | None) -> bool:
    return (value or "").strip().casefold() in {"1", "true", "yes", "on"}


def _load_event(path: str) -> dict[str, Any]:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise LifecycleTelemetryError("event_invalid", "GitHub event must be an object")
    return data


def _fetch_comments(event: dict[str, Any], github_token: str) -> list[str]:
    repository = event["repository"]["full_name"]
    number = event["pull_request"]["number"]
    bodies: list[str] = []
    for page in range(1, 11):
        request = urllib.request.Request(
            f"https://api.github.com/repos/{repository}/issues/{number}/comments"
            f"?per_page=100&page={page}",
            headers={
                "Accept": "application/vnd.github+json",
                "Authorization": f"Bearer {github_token}",
                "X-GitHub-Api-Version": "2022-11-28",
                "User-Agent": "adaptive-agent-workflow",
            },
        )
        try:
            with urllib.request.urlopen(request, timeout=20) as response:
                comments = json.load(response)
        except (urllib.error.URLError, json.JSONDecodeError) as error:
            raise LifecycleTelemetryError(
                "comments_unavailable", "unable to read pull request comments"
            ) from error
        if not isinstance(comments, list):
            raise LifecycleTelemetryError(
                "comments_unavailable", "pull request comments response is invalid"
            )
        bodies.extend(
            item.get("body", "") for item in comments if isinstance(item, dict)
        )
        if len(comments) < 100:
            return bodies
    raise LifecycleTelemetryError(
        "comments_ambiguous", "pull request has too many comments to inspect safely"
    )


def main() -> int:
    if not _enabled(os.getenv("AWF_TELEMETRY_ENABLED")):
        warning("telemetry is disabled; lifecycle dispatch skipped")
        return 0
    target = (os.getenv("AWF_CONTROL_TOWER_REPOSITORY") or "").strip()
    control_tower_token = os.getenv("AWF_CONTROL_TOWER_TOKEN") or ""
    github_token = os.getenv("GITHUB_TOKEN") or ""
    event_path = os.getenv("GITHUB_EVENT_PATH") or ""
    missing = [
        name
        for name, value in (
            ("AWF_CONTROL_TOWER_REPOSITORY", target),
            ("AWF_CONTROL_TOWER_TOKEN", control_tower_token),
            ("GITHUB_TOKEN", github_token),
            ("GITHUB_EVENT_PATH", event_path),
        )
        if not value
    ]
    if missing:
        warning("missing configuration: " + ", ".join(missing))
        return 0
    try:
        event = _load_event(event_path)
        episode = extract_episode_payload(_fetch_comments(event, github_token))
        payload = build_lifecycle_payload(event, episode)
        dispatch_repository_event(target, control_tower_token, payload)
    except (LifecycleTelemetryError, KeyError, OSError, json.JSONDecodeError) as error:
        warning(f"lifecycle dispatch skipped: {error}")
        return 0
    print("AWF lifecycle telemetry dispatched")
    return 0


if __name__ == "__main__":
    sys.exit(main())
