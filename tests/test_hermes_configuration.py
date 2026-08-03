from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_hermes_team_configuration_is_complete_and_non_secret() -> None:
    policy = json.loads((ROOT / ".agent-workflow.json").read_text(encoding="utf-8"))
    team = policy["hermes_team"]
    assert team["enabled"] is True
    assert team["project"] == "Skydonia/awf-e2e-test"
    assert team["roles"] == ["context", "delivery", "review"]
    assert set(team["models"]) == {"context", "delivery", "review"}
    serialized = json.dumps(team).lower()
    assert all(name not in serialized for name in ("token", "password", "api_key", "secret"))


def test_bootstrap_and_project_pin_same_awf_release() -> None:
    project = (ROOT / "pyproject.toml").read_text(encoding="utf-8")
    setup = (ROOT / ".agent/setup-awf.sh").read_text(encoding="utf-8")
    assert "adaptive-agent-workflow==0.1.14" in project
    assert 'adaptive-agent-workflow==0.1.14' in setup
