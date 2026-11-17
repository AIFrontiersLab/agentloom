"""Errors raised by Budget Policy Learner. They are ``StageError`` subclasses so the
orchestrator applies its standard retry, breaker, and fallback semantics."""

from __future__ import annotations

from agent_budget_controller.kernel.errors import StageError


class BudgetPolicyLearnerError(StageError):
    code = "budget_policy_learner_error"

    def __init__(self, message: str, *, retryable: bool = False, details: dict | None = None) -> None:
        super().__init__("budget_policy_learner", message, retryable=retryable, details=details)


class BudgetPolicyLearnerContractViolation(BudgetPolicyLearnerError):
    code = "budget_policy_learner_contract_violation"
