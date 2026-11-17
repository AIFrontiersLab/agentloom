"""Convenience entry points for embedding the pipeline in another program.

    >>> from agent_budget_controller.application.pipeline import run
    >>> result = run({"query": "example", "evidence_ids": ["doc-1"]})
    >>> result["abstain"]
    False
"""

from __future__ import annotations

from agent_budget_controller.application.commands import RunPipeline


def run(request: dict, *, container=None) -> dict:
    """Execute one request against a fresh (or supplied) container and return the outcome dict."""
    if container is None:
        from agent_budget_controller.container import build_container

        container = build_container()
    return container.bus.handle(RunPipeline(request=request))
