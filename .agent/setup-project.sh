#!/usr/bin/env bash
set -euo pipefail
python -m pip install -e ".[dev]" || python -m pip install -e .
python -m pip install build

