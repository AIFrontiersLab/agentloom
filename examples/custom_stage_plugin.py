"""Register a custom stage and insert it before answer assembly."""

from agent_budget_controller.config.settings import Settings
from agent_budget_controller.container import build_container
from agent_budget_controller.plugins.registry import StageRegistry
from agent_budget_controller.stage_catalog import register_all
from agent_budget_controller.stages.base import Stage


class FreshnessBoost(Stage):
    role = "score"

    def process(self, ctx):
        for cand in ctx.candidates:
            cand.score = round(cand.score + 0.05 * float(cand.metadata.get("recent", 0)), 6)
        ctx.candidates.sort(key=lambda c: (-c.score, c.doc_id))
        ctx.decide(self.name, "boosted")


registry = StageRegistry()
register_all(registry)
registry.register("freshness_boost", "score", lambda s: FreshnessBoost("freshness_boost", s), source="plugin")

settings = Settings()
settings.pipeline.stages.insert(len(settings.pipeline.stages) - 1, "freshness_boost")
container = build_container(settings, registry=registry)
print([s.name for s in container.stages])
