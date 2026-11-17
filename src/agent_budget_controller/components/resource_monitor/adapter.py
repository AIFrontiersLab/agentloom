"""Port and registry adapter for Resource Monitor.

Interface from the architecture specification: ``process(ctx) -> None``
"""

from __future__ import annotations

from typing import Protocol

from agent_budget_controller.components.resource_monitor.config import CONFIG
from agent_budget_controller.components.resource_monitor.service import ResourceMonitorService
from agent_budget_controller.domain.models import PipelineContext

ROLE = CONFIG.role


class ResourceMonitorPort(Protocol):
    """Contract the orchestrator relies on."""

    name: str
    role: str

    def process(self, ctx: PipelineContext) -> None: ...

    def describe(self) -> dict: ...


def build(services) -> ResourceMonitorService:
    return ResourceMonitorService(services)
