"""Port and registry adapter for Decision Engine.

Interface from the architecture specification: ``process(ctx) -> None``
"""

from __future__ import annotations

from typing import Protocol

from agent_budget_controller.components.decision_engine.config import CONFIG
from agent_budget_controller.components.decision_engine.service import DecisionEngineService
from agent_budget_controller.domain.models import PipelineContext

ROLE = CONFIG.role


class DecisionEnginePort(Protocol):
    """Contract the orchestrator relies on."""

    name: str
    role: str

    def process(self, ctx: PipelineContext) -> None: ...

    def describe(self) -> dict: ...


def build(services) -> DecisionEngineService:
    return DecisionEngineService(services)
