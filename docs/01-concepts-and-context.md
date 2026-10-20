# 1. Concepts and context

[Guide home](../README.md) · [Next: architecture](02-architecture-and-learning.md) · [Paper map](05-paper-map.md)

## The problem Sophia chooses

An agent can solve a task and still have no durable reason to start another one. The paper's motivating distinction is between externally assigned work and an ongoing goal-feedback process. Sophia adds a supervisor that uses remembered episodes and a model of its own competence to propose the next objective. This is a design framing, not a survey result showing that all other agents are static. [§1, pp. 2–3](https://arxiv.org/pdf/2512.18202v1#page=2).

“Persistence” therefore includes several separable ideas: stored history survives interactions; objectives continue beyond one prompt; behavior remains related to a long-term identity; and future plans use what happened earlier. A process staying alive does not establish all four. The pilot illustrates parts of this bundle in a browser sandbox.

## Three layers as responsibilities

| Layer | Responsibility in this paper | Useful concrete question |
| --- | --- | --- |
| System 1 | Encode observations and execute primitive actions | What happened, and which tool operation can execute a command? |
| System 2 | Deliberately plan toward the current goal | Which sequence of operations might solve this task? |
| System 3 | Select and supervise goals, context, memory, and reward | Why this goal now, and what should this episode change? |

The labels borrow from cognitive theory, but their assignment to software modules is an analogy. They are not measurements of biological subsystems. See [§§1, 3–4, pp. 2–9](https://arxiv.org/pdf/2512.18202v1#page=5). Module 2 explains their interfaces.

## Four psychological pillars

**Theory of mind** motivates maintaining a changing model of another actor's goals, knowledge, and likely behavior. In software this becomes user modeling. Inferring a preference can help communication, but a stored inference can also be wrong; no validated human mental-state inference benchmark is supplied.

**Episodic memory** means records retain event context, time, action, and outcome rather than only isolated facts. The proposed tiered retrieval separates quick summaries from deeper traces. This explains how earlier experiences could influence later prompts without model retraining.

**Metacognition with a self-model** motivates monitoring decisions and maintaining an inspectable representation of capabilities and state. A capability entry is a claim the system stores about itself, not automatically an independently tested skill.

**Intrinsic motivation** supplies candidate reasons to act when no user task arrives. The text discusses curiosity, mastery, and relatedness; Figure 2 highlights autonomy alongside curiosity and mastery. The executive balances such signals with task feedback. These lists are illustrative design descriptions, not a complete fixed reward specification. [§3 and Figure 2, pp. 5–6](https://arxiv.org/pdf/2512.18202v1#page=5).

## How related work supports the argument

§2.1 situates Sophia against continual learning: architectural expansion, regularization, and replay protect knowledge across tasks. Figure 1 contrasts an external task schedule with an internal goal-feedback loop. This clarifies what Sophia emphasizes, but it is a schematic contrast, not evidence that continual-learning methods cannot generate goals.

§2.2 distinguishes **forward learning**, which changes inference context without changing weights, from **post-training/backward learning**, which updates parameters. Sophia's broad architecture permits both. The pilot uses the former exclusively. Persistent external memory can last across sessions even though the foundation model's parameters remain unchanged. [§2, pp. 3–5](https://arxiv.org/pdf/2512.18202v1#page=3).

## Glossary

| Term | Meaning and boundary |
| --- | --- |
| Persistent agent | Agent designed for continuing goals and accumulated experience; not a biological classification |
| System 3 | Proposed executive supervision of Systems 1 and 2 |
| Narrative identity | Coherence between stored self-description, remembered episodes, goals, and explanations |
| Self-model | Inspectable capability/state/creed representation |
| Terminal creed | Persistent identity constraints; the pilot stores five immutable sentences |
| Intrinsic reward | Internally formulated feedback about drives or identity; not necessarily a numeric scalar in the pilot |
| Extrinsic reward | Environment/verifier feedback about task execution |
| RAG | Retrieval-augmented generation: stored material is retrieved into generation context |
| Forward learning | Inference-time adaptation via context and retrieved experience |
| Backward learning | Parameter-changing training described by the broad architecture |
| Process supervision | Critique of candidate reasoning steps by a guardian model |
| Thought search | Branching over partial plans with values and a stopping budget |

The exact computational construction appears in [module 2](02-architecture-and-learning.md). The [limitations module](04-analysis-and-limitations.md) explains why these mechanisms do not establish consciousness, alignment, or durable general learning.
