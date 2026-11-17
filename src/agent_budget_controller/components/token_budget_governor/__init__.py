"""Token Budget Governor.

Enforces per-request and global token ceilings before evidence reaches the answer stage.
"""

from agent_budget_controller.components.token_budget_governor.adapter import ROLE, build
from agent_budget_controller.components.token_budget_governor.config import CONFIG, TokenBudgetGovernorConfig
from agent_budget_controller.components.token_budget_governor.errors import TokenBudgetGovernorError
from agent_budget_controller.components.token_budget_governor.service import TokenBudgetGovernorService

__all__ = ["CONFIG", "ROLE", "build", "TokenBudgetGovernorConfig", "TokenBudgetGovernorError", "TokenBudgetGovernorService"]
