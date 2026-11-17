"""Pre- and post-conditions for Decision Engine.

Violations are defects, not transient faults, so they are raised as
non-retryable errors and surface as a degraded (or failed, if critical) stage.
"""

from __future__ import annotations

from agent_budget_controller.components.decision_engine.config import DecisionEngineConfig
from agent_budget_controller.components.decision_engine.errors import DecisionEngineContractViolation
from agent_budget_controller.components.decision_engine.models import DecisionEngineInput


def validate_input(ctx, config: DecisionEngineConfig) -> None:
    if len(ctx.candidates) > config.max_input_candidates:
        raise DecisionEngineContractViolation(
            "too many candidates for decision_engine",
            details={"limit": config.max_input_candidates, "received": len(ctx.candidates)},
        )


def validate_output(ctx, before: DecisionEngineInput, config: DecisionEngineConfig) -> None:
    ids = [c.doc_id for c in ctx.candidates]
    if len(ids) != len(set(ids)):
        raise DecisionEngineContractViolation("duplicate candidate ids after decision_engine")
    if not config.may_introduce_ids:
        unexpected = set(ids) - set(before.candidate_ids)
        if unexpected:
            raise DecisionEngineContractViolation(
                "decision_engine introduced unknown candidates", details={"ids": sorted(unexpected)}
            )
    if config.enforce_sorted_output and not ctx.cache_hit:
        scores = [c.score for c in ctx.candidates]
        if scores != sorted(scores, reverse=True):
            raise DecisionEngineContractViolation("decision_engine produced an unsorted ranking")
