# 6. Discussion and evaluation

[Guide home](../README.md) · [Previous: source map](05-paper-map.md)

This module contains companion explanations, questions, and proposed experiments. None is an experiment conducted by the paper or this repository.

## Work through one hypothetical episode

Suppose a browser API changes and a previously useful command fails. System 1 delivers the error event; System 2 has a current task but cannot execute its old plan. System 3 can retrieve earlier failures, consult a capability record, and propose learning the changed API. Search compares ways to obtain reliable documentation, supervision critiques the plan, and the planner executes a bounded repair task. Reflection stores what was tried and whether the verifier accepted it.

This paraphrases the design pattern in [§4.2, p. 9](https://arxiv.org/pdf/2512.18202v1#page=9). It is not a trace from the pilot. The central question is whether the update improves an independently checked future task, rather than merely adding a favorable capability description.

If later execution succeeds by retrieving the repair plan, that is forward learning through context. If an optimizer changes the planner's weights using collected episodes, that would be a different training procedure. The pilot only claims the first.

## Questions to check understanding

1. **What makes System 3 different from a longer prompt?** It is proposed as a continuing controller of goals, memory, rewards, and context. The paper does not isolate which part requires a separate layer.
2. **Does a stored self-model prove self-awareness?** No. It makes internal state claims inspectable; their correctness and psychological interpretation require additional evidence.
3. **Does 20% to 60% mean a 40% relative improvement?** No. It is +40 percentage points; relative growth from that baseline is 200%. Denominators and uncertainty remain missing.
4. **Why can fewer reasoning steps coexist with higher total cost?** Retrieval, search workers, critique, and reflection can add work outside the plotted step metric.
5. **Why is idle activity not enough to prove improvement?** An agent can generate many low-value tasks; independent outcomes must assess quality.
6. **What does the creed demonstrate?** An identity constraint the implementation refers to. The selected examples do not establish comprehensive compliance.
7. **Which experimental duration should a citation use?** State the conflict: introduction 24h, quantitative/qualitative material 36h. Do not invent a reconciliation.

## A proposed evaluation plan

| Question | Comparison that would help | Outcome to measure |
| --- | --- | --- |
| Does episodic retrieval help? | Same tasks/model/budget with retrieval on vs off | Success on matched held-out tasks, total calls/tokens/time, retrieval errors |
| Does self-directed goal selection help? | Internal scheduler vs externally supplied goals under equal resources | Independently verified skill gain and useful activity |
| Does the self-model add value? | Capability-aware scheduling vs equivalent memory without the capability dictionary | Calibration of skill claims, transfer, failure recovery |
| Does critique improve decisions? | Same search with and without guardian under matched total compute | Invalid actions, task success, missed failures |
| Does persistence remain coherent? | Multiple long deployments with interruptions and contradictory memories | Recovery, creed compliance, stale-memory harm, performance retention |
| Does the architecture generalize? | New browser domains and, separately, embodied tasks | Task-specific outcomes and boundary failures |

Use multiple independent runs, release the exact task inventory and verifier, report denominators and uncertainty, and separate repeated-task caching from transfer to unseen problems. Track whether useful memory is actually retrieved and whether reward language predicts verified outcomes. These are companion recommendations motivated by the gaps in [§5, pp. 9–14](https://arxiv.org/pdf/2512.18202v1#page=9).

## How to discuss the paper fairly

A defensible statement is: “Sophia proposes a persistent supervisory architecture and illustrates memory reuse and self-generated activity in a small browser pilot.” A claim that it proves artificial life, autonomous lifelong competence, or reliable safety goes beyond the reported study.

When citing the research, use [the pinned v1 paper](https://arxiv.org/abs/2512.18202v1), credit all three authors, and retain the distinction between design, observation, and interpretation.
