"""Pre- and post-conditions for Budget Policy Learner.

Violations are defects, not transient faults, so they are raised as
non-retryable errors and surface as a degraded (or failed, if critical) stage.
"""

from __future__ import annotations

from agent_budget_controller.components.budget_policy_learner.config import BudgetPolicyLearnerConfig
from agent_budget_controller.components.budget_policy_learner.errors import BudgetPolicyLearnerContractViolation
from agent_budget_controller.components.budget_policy_learner.models import BudgetPolicyLearnerInput


def validate_input(ctx, config: BudgetPolicyLearnerConfig) -> None:
    if len(ctx.candidates) > config.max_input_candidates:
        raise BudgetPolicyLearnerContractViolation(
            "too many candidates for budget_policy_learner",
            details={"limit": config.max_input_candidates, "received": len(ctx.candidates)},
        )


def validate_output(ctx, before: BudgetPolicyLearnerInput, config: BudgetPolicyLearnerConfig) -> None:
    ids = [c.doc_id for c in ctx.candidates]
    if len(ids) != len(set(ids)):
        raise BudgetPolicyLearnerContractViolation("duplicate candidate ids after budget_policy_learner")
    if not config.may_introduce_ids:
        unexpected = set(ids) - set(before.candidate_ids)
        if unexpected:
            raise BudgetPolicyLearnerContractViolation(
                "budget_policy_learner introduced unknown candidates", details={"ids": sorted(unexpected)}
            )
    if config.enforce_sorted_output and not ctx.cache_hit:
        scores = [c.score for c in ctx.candidates]
        if scores != sorted(scores, reverse=True):
            raise BudgetPolicyLearnerContractViolation("budget_policy_learner produced an unsorted ranking")
