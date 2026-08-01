#!/usr/bin/env bash
set -euo pipefail
python -m pip install "adaptive-agent-workflow==0.1.3"
python -m pip install -e ".[dev]" || python -m pip install -e .
python -m pip install build
