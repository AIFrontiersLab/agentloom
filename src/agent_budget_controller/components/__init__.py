"""Concept-specific components. Each one specialises a stage role with its own
configuration, validation, metrics, and errors."""

from agent_budget_controller.components.budget_policy_learner import adapter as _budget_policy_learner
from agent_budget_controller.components.decision_engine import adapter as _decision_engine
from agent_budget_controller.components.ranking_cache import adapter as _ranking_cache
from agent_budget_controller.components.resource_monitor import adapter as _resource_monitor
from agent_budget_controller.components.signal_enricher import adapter as _signal_enricher
from agent_budget_controller.components.token_budget_governor import adapter as _token_budget_governor

COMPONENT_FACTORIES = {
    "resource_monitor": (_resource_monitor.ROLE, _resource_monitor.build),
    "budget_policy_learner": (_budget_policy_learner.ROLE, _budget_policy_learner.build),
    "decision_engine": (_decision_engine.ROLE, _decision_engine.build),
    "signal_enricher": (_signal_enricher.ROLE, _signal_enricher.build),
    "ranking_cache": (_ranking_cache.ROLE, _ranking_cache.build),
    "token_budget_governor": (_token_budget_governor.ROLE, _token_budget_governor.build),
}
