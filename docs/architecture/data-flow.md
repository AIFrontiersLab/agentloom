# Data flow

1. Agent initiates an action (LLM call or Tool use).
2. Decision Engine checks current resource usage against the active Policy.
3. If within limits, action proceeds; Resource Monitor logs the delta.
4. Resource Monitor sends usage data to the Budget Policy Learner.
5. Learner updates its internal state and potentially refines the Policy based on reward signals (e.g., task success vs. cost).
6. Updated Policy is pushed to the Decision Engine for the next step.

```mermaid
flowchart LR
    client([Client]) --> api[HTTP / CLI adapter]
    api --> bus[[Message bus]]
    bus --> orch{{Orchestrator}}
    orch --> s0["Intake<br/><i>ingest</i>"]
    s0 --> s1["Corpus Retrieval<br/><i>retrieve</i>"]
    s1 --> s2["Signal Enricher<br/><i>enrich</i>"]
    s2 --> s3["Ranking Cache<br/><i>cache</i>"]
    s3 --> s4["Decision Engine<br/><i>score</i>"]
    s4 --> s5["Graceful Fallback<br/><i>fallback</i>"]
    s5 --> s6["Budget Policy Learner<br/><i>policy</i>"]
    s6 --> s7["Token Budget Governor<br/><i>budget</i>"]
    s7 --> s8["Resource Monitor<br/><i>audit</i>"]
    s8 --> s9["Answer Assembly<br/><i>answer</i>"]
    s9 --> out([Outcome: answer or abstain])
    orch -.-> obs[(Metrics / traces / audit)]
    orch -.-> store[(Run repository)]
```

The `PipelineContext` is the only mutable object in a run. Stages read the request,
mutate candidates, and append decisions. Nothing else carries run state.
