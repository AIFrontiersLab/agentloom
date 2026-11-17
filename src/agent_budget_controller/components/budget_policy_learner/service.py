"""Budget Policy Learner service.

Role: ``policy``. Fail-closed tenant, clearance, and ACL filtering plus PII redaction.

Responsibility (from the architecture specification):
    Fail-closed tenant, clearance, and ACL filtering plus PII redaction.

The service specialises :class:`PolicyStage` and wraps it with this
component's contract checks, metrics, and per-run report.
"""

from __future__ import annotations

from agent_budget_controller.components.budget_policy_learner.config import CONFIG, BudgetPolicyLearnerConfig
from agent_budget_controller.components.budget_policy_learner.models import BudgetPolicyLearnerInput, BudgetPolicyLearnerReport
from agent_budget_controller.components.budget_policy_learner.validators import validate_input, validate_output
from agent_budget_controller.stages.policy import PolicyStage

METRIC_PREFIX = "component_budget_policy_learner"
RUNS = f"{METRIC_PREFIX}_runs_total"
CANDIDATES_OUT = f"{METRIC_PREFIX}_candidates_out"
REMOVED = f"{METRIC_PREFIX}_removed_total"


def record_metrics(metrics, report: BudgetPolicyLearnerReport) -> None:
    if metrics is None:
        return
    metrics.inc(RUNS)
    metrics.observe(CANDIDATES_OUT, report.candidates_out)
    if report.removed:
        metrics.inc(REMOVED, len(report.removed))


class BudgetPolicyLearnerService(PolicyStage):
    def __init__(self, services, config: BudgetPolicyLearnerConfig = CONFIG) -> None:
        super().__init__(config.name, services, description=config.responsibility)
        self.config = config

    def process(self, ctx) -> None:
        validate_input(ctx, self.config)
        before = BudgetPolicyLearnerInput.from_context(ctx)
        super().process(ctx)
        if ctx.halted and not ctx.candidates:
            report = BudgetPolicyLearnerReport.diff(self.name, before, [], halted=True)
        else:
            validate_output(ctx, before, self.config)
            report = BudgetPolicyLearnerReport.diff(self.name, before, [c.doc_id for c in ctx.candidates])
        ctx.metadata.setdefault("reports", {})[self.name] = report.to_dict()
        record_metrics(self.services.metrics, report)

    def describe(self) -> dict:
        info = super().describe()
        info.update({"display_name": self.config.display_name, "interface": self.config.interface})
        return info
