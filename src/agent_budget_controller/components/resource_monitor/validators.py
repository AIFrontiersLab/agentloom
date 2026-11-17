"""Pre- and post-conditions for Resource Monitor.

Violations are defects, not transient faults, so they are raised as
non-retryable errors and surface as a degraded (or failed, if critical) stage.
"""

from __future__ import annotations

from agent_budget_controller.components.resource_monitor.config import ResourceMonitorConfig
from agent_budget_controller.components.resource_monitor.errors import ResourceMonitorContractViolation
from agent_budget_controller.components.resource_monitor.models import ResourceMonitorInput


def validate_input(ctx, config: ResourceMonitorConfig) -> None:
    if len(ctx.candidates) > config.max_input_candidates:
        raise ResourceMonitorContractViolation(
            "too many candidates for resource_monitor",
            details={"limit": config.max_input_candidates, "received": len(ctx.candidates)},
        )


def validate_output(ctx, before: ResourceMonitorInput, config: ResourceMonitorConfig) -> None:
    ids = [c.doc_id for c in ctx.candidates]
    if len(ids) != len(set(ids)):
        raise ResourceMonitorContractViolation("duplicate candidate ids after resource_monitor")
    if not config.may_introduce_ids:
        unexpected = set(ids) - set(before.candidate_ids)
        if unexpected:
            raise ResourceMonitorContractViolation(
                "resource_monitor introduced unknown candidates", details={"ids": sorted(unexpected)}
            )
    if config.enforce_sorted_output and not ctx.cache_hit:
        scores = [c.score for c in ctx.candidates]
        if scores != sorted(scores, reverse=True):
            raise ResourceMonitorContractViolation("resource_monitor produced an unsorted ranking")
