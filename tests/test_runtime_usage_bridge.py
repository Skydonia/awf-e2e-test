from __future__ import annotations

from agentic_workflow.episode_telemetry import episode_v1_payload
from agentic_workflow.episodes import EpisodeStore
from agentic_workflow.models import GitHubMetrics
from agentic_workflow.runtime import publish_runtime_usage_snapshot
from agentic_workflow.storage import Database
from agentic_workflow.usage import UsageMeasurement


def _start_episode(store: EpisodeStore, *, task: str):
    return store.start(
        repository_id="awf-e2e-test",
        task=task,
        workflow_version="0.1.13",
        model="gpt-e2e-runtime",
        github=GitHubMetrics(repository="Skydonia/awf-e2e-test"),
    )


def test_runtime_usage_snapshot_is_episode_scoped_and_idempotent(
    tmp_path,
    monkeypatch,
) -> None:
    store = EpisodeStore(Database(tmp_path / "state"))
    episode = _start_episode(store, task="runtime usage smoke")
    snapshot = tmp_path / "usage.json"

    publish_runtime_usage_snapshot(
        snapshot,
        episode_id=episode.id,
        runtime="awf-e2e-fixture",
        usage=UsageMeasurement(
            input_tokens=1_200,
            output_tokens=300,
            cache_read_tokens=100,
            cache_write_tokens=0,
            estimated_cost_usd=0.0123,
            usage_source="e2e-runtime-fixture",
            usage_quality="observed",
            pricing_version="e2e-native-v1",
            model="gpt-e2e-runtime",
        ),
    )
    monkeypatch.setenv("AWF_RUNTIME_USAGE_FILE", str(snapshot))

    first = store.finish(episode.id, outcome="success", tool_calls=4)
    second = store.finish(episode.id, outcome="success", tool_calls=4)

    assert first.telemetry.input_tokens == 1_200
    assert first.telemetry.output_tokens == 300
    assert first.telemetry.cache_read_tokens == 100
    assert first.telemetry.cache_write_tokens == 0
    assert first.telemetry.estimated_cost_usd == 0.0123
    assert first.telemetry.usage_source == "e2e-runtime-fixture"
    assert first.telemetry.usage_quality == "observed"
    assert first.telemetry.pricing_version == "e2e-native-v1"

    assert second.telemetry.input_tokens == first.telemetry.input_tokens
    assert second.telemetry.output_tokens == first.telemetry.output_tokens
    assert second.telemetry.estimated_cost_usd == first.telemetry.estimated_cost_usd

    payload = episode_v1_payload(second)
    assert payload["usage"] == {
        "usage_schema_version": 1,
        "input_tokens": 1_200,
        "output_tokens": 300,
        "cache_read_tokens": 100,
        "cache_write_tokens": 0,
        "estimated_cost_usd": 0.0123,
        "usage_source": "e2e-runtime-fixture",
        "usage_quality": "observed",
        "pricing_version": "e2e-native-v1",
        "model_calls": None,
        "tool_calls": 4,
        "files_read": None,
        "retries": 0,
        "semantic_iterations": None,
    }


def test_runtime_usage_snapshot_rejects_another_episode(
    tmp_path,
    monkeypatch,
) -> None:
    store = EpisodeStore(Database(tmp_path / "state"))
    episode = _start_episode(store, task="runtime mismatch smoke")
    snapshot = tmp_path / "usage.json"

    publish_runtime_usage_snapshot(
        snapshot,
        episode_id="another-episode",
        runtime="awf-e2e-fixture",
        usage=UsageMeasurement(
            input_tokens=10,
            output_tokens=5,
            usage_source="e2e-runtime-fixture",
            usage_quality="observed",
            model="gpt-e2e-runtime",
        ),
    )
    monkeypatch.setenv("AWF_RUNTIME_USAGE_FILE", str(snapshot))

    finished = store.finish(episode.id, outcome="success")

    assert finished.telemetry.input_tokens is None
    assert finished.telemetry.output_tokens is None
    assert finished.telemetry.estimated_cost_usd is None
    assert finished.telemetry.usage_quality == "unavailable"
    assert finished.telemetry.usage_source == "runtime-file:episode-mismatch"
