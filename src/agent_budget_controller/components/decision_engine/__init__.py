"""Decision Engine.

Blends upstream prior scores with query-aware relevance and reorders candidates.
"""

from agent_budget_controller.components.decision_engine.adapter import ROLE, build
from agent_budget_controller.components.decision_engine.config import CONFIG, DecisionEngineConfig
from agent_budget_controller.components.decision_engine.errors import DecisionEngineError
from agent_budget_controller.components.decision_engine.service import DecisionEngineService

__all__ = ["CONFIG", "ROLE", "build", "DecisionEngineConfig", "DecisionEngineError", "DecisionEngineService"]
