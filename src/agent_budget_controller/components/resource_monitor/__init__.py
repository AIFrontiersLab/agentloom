"""Resource Monitor.

Appends an immutable, redacted audit record of what the run saw and decided.
"""

from agent_budget_controller.components.resource_monitor.adapter import ROLE, build
from agent_budget_controller.components.resource_monitor.config import CONFIG, ResourceMonitorConfig
from agent_budget_controller.components.resource_monitor.errors import ResourceMonitorError
from agent_budget_controller.components.resource_monitor.service import ResourceMonitorService

__all__ = ["CONFIG", "ROLE", "build", "ResourceMonitorConfig", "ResourceMonitorError", "ResourceMonitorService"]
