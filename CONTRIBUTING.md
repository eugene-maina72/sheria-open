# Contributing to SheriaOpen

Thank you for helping make Kenyan legal information more understandable and verifiable.

SheriaOpen welcomes technical, legal, linguistic, design, documentation, accessibility and community contributions. Because the project deals with legal information, some contributions require stronger evidence and review than an ordinary application change.

## Ways to contribute

You can help by:

- writing or reviewing Python code;
- improving ingestion and retrieval;
- creating evaluation questions;
- identifying official legal sources;
- reviewing legal explanations and document status;
- translating reviewed material into Kiswahili;
- improving accessibility and mobile usability;
- reporting unclear, outdated or unsupported answers;
- improving documentation;
- conducting security and privacy reviews; or
- helping maintain community processes.

## Before starting

1. Read the README, Code of Conduct, Governance policy and relevant documentation.
2. Search existing issues and pull requests.
3. Open an issue before beginning a substantial change.
4. Do not upload confidential client files, personal case documents or sensitive user conversations.
5. Do not copy third-party legal summaries or proprietary datasets without permission.

## Contribution categories

### Software changes

Software changes should include appropriate tests and should not weaken citation validation, source restrictions, privacy controls or legal-status checks.

### Legal-content changes

A legal-content contribution must identify:

- the official document title;
- the exact article, section, subsection or schedule;
- the official source URL;
- the document's status;
- the effective or version date, where relevant;
- the date on which the source was verified;
- any important exception or limitation; and
- whether the contribution has received legal review.

News reports, political statements, social-media posts and general blogs are not acceptable as the sole authority for a legal proposition.

### Translation changes

Translations should preserve legal meaning rather than translate word-for-word. A translated answer should remain linked to the reviewed source-language explanation and official legal provision. Material changes to meaning require renewed legal review.

### Evaluation changes

Evaluation examples should test more than fluency. Useful cases include:

- confusion between a Bill and an enacted Act;
- repealed or amended provisions;
- commencement-date questions;
- conflicting retrieved passages;
- missing evidence;
- Kiswahili ambiguity;
- prompt injection inside retrieved documents; and
- high-risk personal scenarios that should be escalated.

## Development setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -e ".[dev]"
pre-commit install
```

Run checks:

```bash
ruff check .
ruff format --check .
mypy src
pytest
```

## Branch and commit conventions

Use a focused branch name:

```text
feature/constitution-ingestion
fix/citation-validation
legal-review/article-35
translation/swahili-rights
```

Prefer Conventional Commit-style messages:

```text
feat: add section-aware Constitution parser
fix: reject citations absent from retrieved context
docs: clarify legal-status labels
test: add repealed-law evaluation cases
```

## Pull-request requirements

A pull request should:

- explain the problem and the proposed change;
- reference the relevant issue;
- include tests or explain why none are required;
- disclose any new dependency, model or external service;
- identify privacy or security effects;
- complete the legal-content checklist when applicable;
- avoid unrelated formatting changes; and
- pass automated checks.

At least one maintainer approval is required for ordinary changes. Changes to legal explanations, source policy or status resolution should also receive review from an approved domain reviewer before release.

## Licence of contributions

By submitting a contribution, you confirm that:

- you created the contribution or have the right to submit it;
- the contribution may be distributed under the licence applicable to the destination file or directory; and
- you have not knowingly included confidential, unlawfully obtained or incompatible material.

Source code contributions are normally accepted under `AGPL-3.0-or-later`. Documentation or curated content explicitly marked as such may be accepted under `CC-BY-SA-4.0`.

## Attribution

Significant contributors will be recognised through Git history, release notes and, where appropriate, `CONTRIBUTORS.md`.

## Questions

Use a GitHub discussion or a narrowly scoped issue for public project questions. Report security vulnerabilities privately according to `SECURITY.md`.
