# 4. Analysis and limitations

[Guide home](../README.md) · [Previous: pilot](03-pilot-and-evidence.md) · [Next: source map](05-paper-map.md)

## What the contribution can support

The paper offers an architectural vocabulary for connecting ongoing goal selection, contextual memory, reflection, social modeling, and self-description. The pilot illustrates that a browser agent can persist records, retrieve a plan, and remain active without a fresh user command. This is a useful feasibility narrative. The conclusion itself describes a small pilot and calls for more comprehensive research. [§6, p. 14](https://arxiv.org/pdf/2512.18202v1#page=14).

The stronger claims about reliable lifelong improvement, performance beyond static-model limits, and trustworthy artificial life are interpretations or ambitions. A modular architecture and selected traces do not demonstrate them as general properties. This distinction is especially important when reading confident language in the abstract and figure captions.

## Evidence limits

A single agent is not necessarily a single model call; it can invoke many workers. Yet the paper does not provide independent-agent replications, task denominators, checkpoint-equivalent task sets, uncertainty, or controlled comparisons. It explicitly defers larger pools and systematic ablations. Apparent growth could mix practice, changed task composition, retrieval advantages, and supervisor behavior. The pilot does not isolate these mechanisms. [§5 introduction, pp. 9–10](https://arxiv.org/pdf/2512.18202v1#page=9).

The “baseline would stop” account is not a measured competing architecture. Similarly, the claim that a reduction is directly attributable to memory is not supported by a memory-disabled control. Reasoning-step savings also omit the executive's search, critique, reflection, and retrieval costs.

## Specification and reproducibility gaps

The formal model makes interfaces legible but leaves substantial engineering choices open: concrete planner/guardian models, prompts, search budgets, utility estimation, retrieval thresholds, memory schema, task inventory, verifier rules, and complete creed text. Natural-language reward concatenation does not explain how numerical weighting is implemented consistently. The source gives no linked code repository or released raw logs that would close these gaps.

The general gradient-update path is a proposal; the pilot uses retrieved context. A self-model update is a change in a stored description. Neither should be called model-weight training. The 24h/36h and task-count conflicts further limit precise reconstruction. See [module 3](03-pilot-and-evidence.md).

## Identity and psychological language

A consistent story about earlier episodes is an operational interpretation of identity continuity. It is not evidence of subjective experience or conscious self-awareness. The paper's psychological constructs motivate software responsibilities; the pilot does not validate them as faithful cognitive mechanisms.

Stored user beliefs need correction rules and uncertainty. A synthetic feed indicating stress is not a test of reliable mental-state inference. Descriptions of creed-linked helpfulness do not establish measured human benefit. These are companion analytical distinctions, not new empirical results.

## Safety and incentives

A guardian LLM can make correlated errors with the planner. An immutable creed can be underspecified. A self-issued reward can favor convincing explanations or repeated easy activity over actual competence. The pilot supplies no adversarial safety evaluation, privacy study, reward-hacking test, or verification of long-term incentive stability.

These gaps do not prove the architecture unsafe; they limit its safety claims. A practical design would need independently checked outcomes, bounded actions, editable user inferences, and the ability to halt goal generation. Those are companion recommendations, not mechanisms validated in the paper.

## Scope of generalization

The controlled offline browser is not an open-world deployment, physical robot, or human-participant trial. Robotic migration is future work. Continuous operation over the reported horizon does not establish indefinite persistence, recovery from corrupt memory, successful transfer to new domains, or retention after many interacting goals. [§5, pp. 9–10](https://arxiv.org/pdf/2512.18202v1#page=9).

A productive reading stance is to assess the architecture as a proposal and the pilot as an illustration, then ask what experiments could distinguish its mechanisms. [Module 6](06-discussion-and-evaluation.md) supplies a clearly labeled evaluation plan.
