"""Resource Monitor service.

Role: ``audit``. Appends an immutable, redacted audit record of what the run saw and decided.

Responsibility (from the architecture specification):
    Appends an immutable, redacted audit record of what the run saw and decided.

The service specialises :class:`AuditStage` and wraps it with this
component's contract checks, metrics, and per-run report.
"""

from __future__ import annotations

from agent_budget_controller.components.resource_monitor.config import CONFIG, ResourceMonitorConfig
from agent_budget_controller.components.resource_monitor.models import ResourceMonitorInput, ResourceMonitorReport
from agent_budget_controller.components.resource_monitor.validators import validate_input, validate_output
from agent_budget_controller.stages.audit import AuditStage

METRIC_PREFIX = "component_resource_monitor"
RUNS = f"{METRIC_PREFIX}_runs_total"
CANDIDATES_OUT = f"{METRIC_PREFIX}_candidates_out"
REMOVED = f"{METRIC_PREFIX}_removed_total"


def record_metrics(metrics, report: ResourceMonitorReport) -> None:
    if metrics is None:
        return
    metrics.inc(RUNS)
    metrics.observe(CANDIDATES_OUT, report.candidates_out)
    if report.removed:
        metrics.inc(REMOVED, len(report.removed))


class ResourceMonitorService(AuditStage):
    def __init__(self, services, config: ResourceMonitorConfig = CONFIG) -> None:
        super().__init__(config.name, services, description=config.responsibility)
        self.config = config

    def process(self, ctx) -> None:
        validate_input(ctx, self.config)
        before = ResourceMonitorInput.from_context(ctx)
        super().process(ctx)
        if ctx.halted and not ctx.candidates:
            report = ResourceMonitorReport.diff(self.name, before, [], halted=True)
        else:
            validate_output(ctx, before, self.config)
            report = ResourceMonitorReport.diff(self.name, before, [c.doc_id for c in ctx.candidates])
        ctx.metadata.setdefault("reports", {})[self.name] = report.to_dict()
        record_metrics(self.services.metrics, report)

    def describe(self) -> dict:
        info = super().describe()
        info.update({"display_name": self.config.display_name, "interface": self.config.interface})
        return info
