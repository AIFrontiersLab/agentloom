"""Static configuration for the Budget Policy Learner component."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class BudgetPolicyLearnerConfig:
    name: str = "budget_policy_learner"
    display_name: str = 'Budget Policy Learner'
    role: str = "policy"
    interface: str = 'process(ctx) -> None'
    responsibility: str = 'Fail-closed tenant, clearance, and ACL filtering plus PII redaction.'
    max_input_candidates: int = 10_000
    may_introduce_ids: bool = False
    enforce_sorted_output: bool = False


CONFIG = BudgetPolicyLearnerConfig()
