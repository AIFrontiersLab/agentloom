"""Errors raised by Resource Monitor. They are ``StageError`` subclasses so the
orchestrator applies its standard retry, breaker, and fallback semantics."""

from __future__ import annotations

from agent_budget_controller.kernel.errors import StageError


class ResourceMonitorError(StageError):
    code = "resource_monitor_error"

    def __init__(self, message: str, *, retryable: bool = False, details: dict | None = None) -> None:
        super().__init__("resource_monitor", message, retryable=retryable, details=details)


class ResourceMonitorContractViolation(ResourceMonitorError):
    code = "resource_monitor_contract_violation"
