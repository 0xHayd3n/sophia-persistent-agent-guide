# 5. Complete paper map

[Guide home](../README.md) · [Previous: limitations](04-analysis-and-limitations.md) · [Next: discussion](06-discussion-and-evaluation.md)

The actual attachment is 16 pages, arXiv:2512.18202v1. One-based PDF page numbers match printed numbers. The title uses **“of Artificial Life”**; the running header uses **“for Artificial Life.”** Bibliographic records preserve the title-page/arXiv title.

## Section coverage

| Source part | PDF pages | Companion coverage |
| --- | --- | --- |
| Title, authors, affiliations, abstract | [1](https://arxiv.org/pdf/2512.18202v1#page=1) | README, attribution, evidence boundaries |
| §1 Introduction | [2–3](https://arxiv.org/pdf/2512.18202v1#page=2) | Module 1: task persistence, cognitive layers, four motivations |
| §2 Related Work; §2.1 Continual Learning | [3–4](https://arxiv.org/pdf/2512.18202v1#page=3) | Module 1: replay, regularization, architecture, internal scheduling |
| §2.2 Forward Learning and Backward Learning in LLMs | [4–5](https://arxiv.org/pdf/2512.18202v1#page=4) | Modules 1–2: context vs parameter changes |
| §3 The Psychological Pillars of System 3 | [5–6](https://arxiv.org/pdf/2512.18202v1#page=5) | Module 1: pillars and architectural analogy |
| §3.1 Foundational Constructs | [6](https://arxiv.org/pdf/2512.18202v1#page=6) | Module 1: ToM, memory, self-model, motivation |
| §3.2 Why These Pillars Matter | [6](https://arxiv.org/pdf/2512.18202v1#page=6) | Modules 1 and 4: adaptation, accumulation, audit as ambitions |
| §4 The Persistent Agent with System 3 in Operation | [6–9](https://arxiv.org/pdf/2512.18202v1#page=6) | Module 2 |
| §4.1 Layered Stack Overview | [7](https://arxiv.org/pdf/2512.18202v1#page=7) | Module 2: data flow and Persistent-POMDP |
| §4.1.1 System 1 | [8](https://arxiv.org/pdf/2512.18202v1#page=8) | Module 2: encoder, primitive actions, external reward |
| §4.1.2 System 2 | [8](https://arxiv.org/pdf/2512.18202v1#page=8) | Module 2: LLM/parser policy and proposed gradient update |
| §4.1.3 System 3 | [8–9](https://arxiv.org/pdf/2512.18202v1#page=8) | Module 2: meta-policy, search/critique/reflection, support services |
| §4.2 Autonomous Cognitive Cycle | [9](https://arxiv.org/pdf/2512.18202v1#page=9) | Modules 2 and 6: remedial-goal example |
| §5 Experiments and its pilot qualification | [9–14](https://arxiv.org/pdf/2512.18202v1#page=9) | Modules 3–4 |
| §5.1.1 Environment; §5.1.2 Agent Implementation | [10](https://arxiv.org/pdf/2512.18202v1#page=10) | Module 3: offline sandbox, feed, creed, memory-only adaptation |
| §5.2.1 Evolutionary Capability Growth | [10–11](https://arxiv.org/pdf/2512.18202v1#page=10) | Module 3: tiers and first-attempt success |
| §5.2.2 Proactive Autonomy; §5.2.3 Cognitive Efficiency | [12](https://arxiv.org/pdf/2512.18202v1#page=12) | Module 3: task provenance and repeated-problem steps |
| §5.3.1 Automatically Generated Sub-Goals | [12](https://arxiv.org/pdf/2512.18202v1#page=12) | Module 3: original paraphrases of examples |
| §5.3.2 Interaction Trajectory | [13](https://arxiv.org/pdf/2512.18202v1#page=13) | Module 3: stress, knowledge push, self-model update |
| §5.3.3 Key Observations | [13–14](https://arxiv.org/pdf/2512.18202v1#page=13) | Modules 3–4: selected narratives vs evaluated consistency |
| §6 Conclusion | [14](https://arxiv.org/pdf/2512.18202v1#page=14) | Module 4 and discussion |
| References | [14–16](https://arxiv.org/pdf/2512.18202v1#page=14) | Reference reading guide below |

**No appendix or supplementary section appears in this v1 attachment. No tables are present.** The last three pages contain references after the conclusion begins on p. 14.

## Figures and mathematical displays

| Item | Page | Reading purpose |
| --- | --- | --- |
| Figure 1 | [4](https://arxiv.org/pdf/2512.18202v1#page=4) | External curriculum vs internal goal-feedback loop; schematic, not benchmark |
| Figure 2 | [5](https://arxiv.org/pdf/2512.18202v1#page=5) | Psychological pillars into executive oversight |
| Figure 3 | [7](https://arxiv.org/pdf/2512.18202v1#page=7) | Layered implementation proposal; includes an RL path unused in the pilot |
| Figure 4 | [11](https://arxiv.org/pdf/2512.18202v1#page=11) | First-attempt success across tiers and checkpoints |
| Figure 5 left | [11](https://arxiv.org/pdf/2512.18202v1#page=11) | Intrinsic/extrinsic task counts; compare disputed prose count |
| Figure 5 right | [11](https://arxiv.org/pdf/2512.18202v1#page=11) | Repeated-problem reasoning-step illustration |
| Persistent-POMDP tuple and definitions | [7](https://arxiv.org/pdf/2512.18202v1#page=7) | State, observation, action, rewards, layered policies, context |
| Encoder/action policy, LLM/parser policy, gradient objective, meta-policy and search selection | [8](https://arxiv.org/pdf/2512.18202v1#page=8) | Proposed interfaces and optimization intent; unnumbered equations |
| Memory-update expression and hybrid-reward discussion | [9](https://arxiv.org/pdf/2512.18202v1#page=9) | Episodic update and reward representation |

Figures 1–5 and the notation were inspected visually in the matching official v1 PDF. The images are linked, not copied into this guide.

## Reference reading guide

The bibliography on pp. 14–16 is part of the source's coverage. It groups naturally into:

- **Cognitive foundations:** Dunlosky and Metcalfe; Shaughnessy, Veenman, and Kennedy; Frith and Frith; Wellman; Tulving; Ezzyat and Davachi; Fishbach and Woolley. These motivate the four pillars.
- **Continual learning:** Ahn et al.; Chaudhry et al.; Lopez-Paz and Ranzato; Lu et al.; Wang et al.; Ke and Liu; Zheng et al. (2025a, 2025b); Zhou et al. These contextualize retention, scheduling, and adaptation.
- **Agent and model context:** GPT-4, Llama 3, GPT-4o, DeepSeek-R1, Qwen3, and agent surveys/platform work cited by the authors. References do not establish which exact models ran in the pilot.
- **Learning and implementation ingredients:** Li on in-context prompts; Bai et al. and Lambert on RLHF; Zhang et al. and Wu et al. on fine-tuning; Feng et al. on natural-language reinforcement learning; Radford et al. on CLIP and Whisper.
- **Artificial life:** Langton's work supplies the broader framing.

These are descriptions of how Sophia uses its bibliography, not claims that this guide independently reviewed every cited work. Consult the original reference list for full records. The guide's [BibTeX](../references/paper.bib) cites the focal paper with all authors.
