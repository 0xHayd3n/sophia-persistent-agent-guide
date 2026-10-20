# Contributing

Corrections should identify arXiv:2512.18202v1, the exact section and one-based PDF page, the current guide statement, and the proposed correction. Explain whether it changes a conceptual claim, pilot observation, or companion interpretation.

Preserve all three authors and the source version. Do not silently reconcile 24h/36h, the abstract's gain wording, or the intrinsic-task count conflict. Add a later source as a new versioned record if it resolves an issue.

Update relevant documents and metadata together. Keep measured results separate from proposed evaluations. Do not upload the paper PDF, full source text, original figures, or copyrighted logs.

Run `python scripts/validate_repository.py` and recheck any changed primary links. The script validates repository integrity, not the research. Unreported model IDs, sample sizes, seeds, uncertainty and code availability must not be invented.
