#!/usr/bin/env bash
set -euo pipefail
python -m pip install "adaptive-agent-workflow==0.1.10"
bash .agent/setup-project.sh
