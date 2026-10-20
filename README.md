# Sophia reading guide

An independent, source-grounded companion to **Sophia: A Persistent Agent Framework of Artificial Life** by **Mingyang Sun, Feng Hong, and Weinan Zhang** (arXiv:2512.18202v1, 20 December 2025).

[Versioned paper](https://arxiv.org/abs/2512.18202v1) · [PDF](https://arxiv.org/pdf/2512.18202v1) · [Citation](CITATION.cff) · [Agent instructions](AGENTS.md) · [Source map](docs/05-paper-map.md)

Sophia asks what an agent needs to keep choosing goals, recalling experiences, and revising its behavior across interactions. The proposed **System 3** supervises perception/action (System 1) and deliberate planning (System 2) through memory, user and self models, thought search, and intrinsic rewards. Its psychological vocabulary is an architectural proposal. It does not establish consciousness, biological life, general intelligence, or guaranteed safety.

The paper is primarily conceptual and includes an exploratory single-agent browser-sandbox pilot. This repository explains both, preserving their different evidence levels. It contains original educational notes, not the authors' implementation, a replication, or the source PDF.

## Start reading

| Module | What you will learn | Primary coverage |
| --- | --- | --- |
| [1. Concepts and context](docs/01-concepts-and-context.md) | Persistence, cognitive layers, four psychological pillars, related work, glossary | §§1–3, pp. 2–6 |
| [2. Architecture and learning](docs/02-architecture-and-learning.md) | Persistent-POMDP notation, layer interfaces, executive routines, memory and reward, autonomous cycle | §4, pp. 6–9 |
| [3. Pilot and reported observations](docs/03-pilot-and-evidence.md) | Actual deployment, metric scope, figures, qualitative examples, reporting discrepancies | §5, pp. 9–14 |
| [4. Analysis and limitations](docs/04-analysis-and-limitations.md) | What follows from the evidence, missing controls, implementation gaps, safety and identity claims | §§3–6 |
| [5. Complete paper map](docs/05-paper-map.md) | Every section, all five figures, equations and reference pages; no appendix | All 16 PDF pages |
| [6. Discussion and evaluation](docs/06-discussion-and-evaluation.md) | Worked reading example, comprehension checks, proposed evaluation plan | Companion analysis, grounded in §§4–6 |

**Quick route:** this README → modules 1 and 3 → limitations.

**Technical route:** module 2 alongside §4 → pilot protocol → limitations → proposed evaluation.

**Source-first route:** use the paper map with the versioned PDF. All page numbers are **one-based PDF pages**, matching printed pages here.

## What the pilot reports

These are author-reported observations from an exploratory pilot, not results produced or independently verified by this repository.

| Observation | Essential qualification | Source |
| --- | --- | --- |
| Hard-task first-attempt success rises from **20% to 60%** | A **40 percentage-point** difference; task counts, uncertainty, matched difficulty, and independent runs are not provided. The abstract's “40% gain” is ambiguous. | [§5.2.1, p. 10](https://arxiv.org/pdf/2512.18202v1#page=10), [Figure 4, p. 11](https://arxiv.org/pdf/2512.18202v1#page=11) |
| Approximately **80% fewer reasoning steps** on recurring operations; later episodes use about **3–4 steps** | A within-run repeated-problem illustration; reasoning steps are not measured tokens, latency, energy, or total system cost. No memory ablation establishes causality. | [§5.2.3, p. 12](https://arxiv.org/pdf/2512.18202v1#page=12), [Figure 5, p. 11](https://arxiv.org/pdf/2512.18202v1#page=11) |
| Self-generated activity continues while the synthetic user is idle | §5.2.2 says **13** intrinsic tasks at 12–18h; the plotted bar appears to reach **12**. No released raw count resolves this discrepancy. | [§5.2.2, p. 12](https://arxiv.org/pdf/2512.18202v1#page=12), [Figure 5, p. 11](https://arxiv.org/pdf/2512.18202v1#page=11) |
| Reuse of stored plans and creed-linked explanations | Selected trajectories illustrate the design. They do not demonstrate human benefit, subjective identity, or reliable self-assessment. | [§5.3, pp. 12–14](https://arxiv.org/pdf/2512.18202v1#page=12) |

**Two distinctions are central:** the general architecture describes possible policy-gradient updates, but the deployed pilot explicitly performs **no runtime parameter updates** (§5.1.2, p. 10). The introduction calls the demonstration **24 hours** (p. 3), whereas quantitative and qualitative sections discuss **36 hours** (pp. 10–13). These inconsistencies are retained and explained in [module 3](docs/03-pilot-and-evidence.md).

## Use with an agent

Read [AGENTS.md](AGENTS.md), then select a module using [LLMS.txt](LLMS.txt). A useful prompt is:

```text
Explain Sophia's proposed learning cycle using the pinned v1 source.
Separate conceptual design, implemented pilot behavior, and companion analysis.
For each numerical claim, give the PDF page, metric, scope, and missing controls.
Explain why memory-based adaptation here does not imply runtime weight training.
```

[Claim metadata](metadata/claims.json) classifies proposals, reported observations, and limitations. [Paper metadata](metadata/paper.json) records all authors, version, provenance, and reporting issues; [sources](metadata/sources.json) distinguishes the actual attachment from official metadata and figure checks.

## Contents and provenance

The repository includes six reading modules, human and agent navigation, bibliographic metadata, structured claims and pilot results, attribution and contribution rules, and an offline integrity validator. [VERIFICATION.md](VERIFICATION.md) records check scope.

The complete actual uploaded 16-page attachment was read through Library. Its version and authors were checked against arXiv. Figures 1–5 and mathematical notation were visually checked in the matching official v1 PDF because the attachment's materialized path was on a separate cloud filesystem. **No source substitution was needed for text; attachment/public-PDF byte identity was not established.** Source files, extracted full text, and figure screenshots are not redistributed.

## Cite and credit

Credit **Sun, Hong, and Zhang (2025)** for the research. [BibTeX](references/paper.bib) and [CITATION.cff](CITATION.cff) preserve all three authors. DOI: [10.48550/arXiv.2512.18202](https://doi.org/10.48550/arXiv.2512.18202).

Hayden / **0xHayd3n** maintains this unofficial companion; the paper authors have not endorsed it. Original companion documentation is licensed under [CC BY 4.0](LICENSE); the validator has its own MIT notice in that file. The source paper has a separate CC BY 4.0 license recorded by arXiv. See [ATTRIBUTION.md](ATTRIBUTION.md) for boundaries.

## Check integrity

```bash
python scripts/validate_repository.py
```

The validator checks files, local links and anchors, JSON references and source-page bounds. It cannot validate the paper's experiments. Corrections should supply exact version, section, and page; see [CONTRIBUTING.md](CONTRIBUTING.md).
