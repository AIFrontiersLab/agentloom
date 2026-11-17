"""Extension points: stage factories and lifecycle hooks."""

from agent_budget_controller.plugins.hooks import HookManager
from agent_budget_controller.plugins.registry import StageRegistry

__all__ = ["HookManager", "StageRegistry"]
