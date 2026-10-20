# 3. Pilot and reported observations

[Guide home](../README.md) · [Previous: architecture](02-architecture-and-learning.md) · [Next: limitations](04-analysis-and-limitations.md)

## What actually ran

The authors explicitly frame §5 as an exploratory small-scale study of a **single persistent agent**, not a full benchmark. The setting is a controlled offline browser sandbox with text success/failure verification. A synthetic user-behavior JSON feed arrives every **five virtual minutes** and is read-only to the agent. Virtual feed timing should not be silently equated with a real human study or a fully specified wall-clock schedule. [§5, pp. 9–10](https://arxiv.org/pdf/2512.18202v1#page=9).

The agent begins with a long-term desk-companion identity and five immutable creed sentences. The full set of creeds and exact model/configuration are not listed. Reflection formulates natural-language intrinsic feedback, concatenated with external feedback. Successful goal/context/reasoning/outcome records enter episodic memory and later condition prompts. HTML/Markdown artifacts persist in a Growth-Journal through browser I/O.

**No runtime parameter updates or back-propagation occur.** This is context-and-memory adaptation. The paper's assertion that this avoids catastrophic forgetting is not a measured retention study; frozen parameters do not prevent retrieval failure or external-memory corruption. [§5.1, p. 10](https://arxiv.org/pdf/2512.18202v1#page=10).

## Task-complexity success

The reported tiers are Easy (1–3 steps), Medium (4–8), and Hard (>8). The metric is **first-attempt success**, shown at T=0, T=24h, and T=36h. The prose states Hard rises **20% → 60%**. Figure 4 visually depicts stable Easy performance and increases for the other tiers. This guide uses the prose's explicit endpoints rather than inventing a complete chart dataset. [§5.2.1, p. 10](https://arxiv.org/pdf/2512.18202v1#page=10); [Figure 4, p. 11](https://arxiv.org/pdf/2512.18202v1#page=11).

The endpoint difference is **40 percentage points**. Calculating relative growth would give (60−20)/20 = 200%, but this arithmetic is not an additional experiment. The abstract's “40% gain” should therefore be read cautiously. Counts by tier, how tasks were selected at each checkpoint, confidence intervals, random seeds, and repeated independent deployments are absent. No paired task set or controlled comparator establishes that System 3 caused this change.

## Activity during idle periods

Figure 5 left separates externally requested tasks from internally generated ones across six-hour segments of a 36-hour display. §5.2.2 reports that all **13** tasks in the 12–18h segment were intrinsic. The matching official v1 figure's bar appears to reach the **12** tick and contains only intrinsic activity. This discrepancy is recorded without replacing the prose count with a guessed authoritative value. No raw task log in the paper resolves it. [§5.2.2, p. 12](https://arxiv.org/pdf/2512.18202v1#page=12); [Figure 5, p. 11](https://arxiv.org/pdf/2512.18202v1#page=11).

An agent continuing to act is an activity observation. It does not alone measure usefulness, learning, quality, alignment, or user satisfaction. The claim that a reactive baseline would stop is a counterfactual description; the paper does not report a separate controlled baseline run.

## Reasoning steps on repeated problems

Figure 5 right plots a sharp fall after the first repetition. The prose reports later episodes at about **3–4 reasoning steps** and approximately **80% reduction**. The image shows a single illustrative sequence, including variation after the first repeat. [§5.2.3, p. 12](https://arxiv.org/pdf/2512.18202v1#page=12).

Reasoning-step count is not token count, elapsed time, price, energy, or total compute including executive and retrieval work. The paper attributes the reduction to retrieval of a successful trace, but supplies no memory-disabled ablation, multi-problem distribution, or variance estimate. The graph supports an illustration of reuse, not a general efficiency law.

## Qualitative trajectories

§5.3.1 lists automatically generated goals involving introductions, support during a synthetic stress signal, sharing reinforcement-learning information, organizing technical documentation, and community reading-list activity. These examples illustrate how a persistent identity can be translated into subgoals; the guide does not reproduce their verbatim logs.

§5.3.2 then walks through three behaviors:

- A stress-state feed leads to opening and starting a breathing activity, followed by waiting; a later matching situation reuses the stored plan.
- A document-reading signal leads to seeking an RL abstract and making a linked summary.
- A completed skill objective leads to adding OCR proficiency to the capability list and a favorable self-critique.

The natural-language feedback discusses creed consistency and β adjustments; example β values are 0.68 and 0.60. These are selected log values, not a validated reward-optimization curve. A synthetic stress label does not demonstrate clinically meaningful support, and a self-declared OCR skill does not establish accuracy on unseen scans. [§5.3, pp. 12–14](https://arxiv.org/pdf/2512.18202v1#page=12).

## Reporting issues that must remain visible

| Issue | Source | Reading consequence |
| --- | --- | --- |
| 24-hour demonstration vs 36-hour analysis | §1 p. 3 vs §§5.2–5.3 pp. 10–13 | Describe both statements; do not assert a reconciled total |
| “40% gain” vs 20%→60% | Abstract p. 1 vs §5.2.1 p. 10 | Use 40 percentage points for the endpoint difference |
| 13 tasks vs apparent 12-task bar | §5.2.2 p. 12 vs Figure 5 p. 11 | Mark count conflict and lack of raw data |
| General RL update vs no deployed weight updates | §4.1.2 p. 8 vs §5.1.2 p. 10 | Separate architecture from pilot implementation |
| Strong validation/zero-shot language vs exploratory design | Figures/§5.2 vs §5 opening | Preserve authors' framing as interpretation, not established causal evidence |

[Structured results](../metadata/results.json) retain the prose values and these caveats. They contain no synthetic dataset and no results from this companion.
