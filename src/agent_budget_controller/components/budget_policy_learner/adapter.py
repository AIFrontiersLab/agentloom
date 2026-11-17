"""Port and registry adapter for Budget Policy Learner.

Interface from the architecture specification: ``process(ctx) -> None``
"""

from __future__ import annotations

from typing import Protocol

from agent_budget_controller.components.budget_policy_learner.config import CONFIG
from agent_budget_controller.components.budget_policy_learner.service import BudgetPolicyLearnerService
from agent_budget_controller.domain.models import PipelineContext

ROLE = CONFIG.role


class BudgetPolicyLearnerPort(Protocol):
    """Contract the orchestrator relies on."""

    name: str
    role: str

    def process(self, ctx: PipelineContext) -> None: ...

    def describe(self) -> dict: ...


def build(services) -> BudgetPolicyLearnerService:
    return BudgetPolicyLearnerService(services)
