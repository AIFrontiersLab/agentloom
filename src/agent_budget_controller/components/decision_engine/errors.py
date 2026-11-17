"""Errors raised by Decision Engine. They are ``StageError`` subclasses so the
orchestrator applies its standard retry, breaker, and fallback semantics."""

from __future__ import annotations

from agent_budget_controller.kernel.errors import StageError


class DecisionEngineError(StageError):
    code = "decision_engine_error"

    def __init__(self, message: str, *, retryable: bool = False, details: dict | None = None) -> None:
        super().__init__("decision_engine", message, retryable=retryable, details=details)


class DecisionEngineContractViolation(DecisionEngineError):
    code = "decision_engine_contract_violation"
