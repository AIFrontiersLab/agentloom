#!/usr/bin/env bash
set -euo pipefail
export AGENT_BUDGET_CONTROLLER_CONFIG=${AGENT_BUDGET_CONTROLLER_CONFIG:-config/development.toml}
PYTHONPATH=src exec python -m agent_budget_controller serve "$@"
