# SheriaOpen

**Kenyan law, open and understandable.**

[![License: AGPL v3 or later](https://img.shields.io/badge/License-AGPL_v3_or_later-blue.svg)](LICENSE)
[![Project status: early development](https://img.shields.io/badge/status-early_development-orange.svg)](docs/ROADMAP.md)
[![Python 3.12+](https://img.shields.io/badge/python-3.12%2B-blue.svg)](pyproject.toml)

SheriaOpen is an open-source Kenyan legal-information platform that helps people understand the Constitution of Kenya, Acts of Parliament, proposed Bills, amendments, commencement notices and repealed laws in plain language.

The platform is designed around retrieval-augmented generation (RAG), locally hosted language models through Ollama, and verifiable citations to official legal sources. Its purpose is civic education and access to legal information—not automated legal representation.

> [!IMPORTANT]
> SheriaOpen provides general legal information only. It does not provide legal advice, create an advocate-client relationship, or replace a qualified Kenyan advocate. Users facing an arrest, court deadline, criminal allegation, eviction, domestic violence, immigration matter or other urgent dispute should obtain professional assistance.

## Project status

SheriaOpen is in **early development**. The first target is a Constitution-only research prototype with reliable retrieval, source citations and legal-status labels. It should not be treated as a production legal service until the release gates in the roadmap have been met.

## What SheriaOpen aims to do

- Explain Kenyan legal provisions in accessible English and Kiswahili.
- Distinguish current law from Bills, repealed law, uncommenced provisions and historical versions.
- Cite the exact official document, article, section or schedule supporting an answer.
- Show when the relevant source was last verified.
- State important exceptions and uncertainty instead of inventing an answer.
- Help users find legitimate public-participation, complaint, legal-aid and professional-support channels.
- Make the software, evaluation methods and corrections process open to public inspection.

## What SheriaOpen will not do

- Recommend political parties or candidates.
- Infer or profile a user's political affiliation.
- Guarantee legal outcomes.
- Generate unsupported statutes, cases, sections or legal status.
- Replace a qualified advocate in an individual legal dispute.
- Treat news articles, political statements or social-media posts as primary legal authority.

## Guiding principles

1. **Official sources first.** Legal answers must be grounded in authoritative material.
2. **Status before summary.** The system must determine whether a document is current law, a Bill, repealed, revoked, expired, uncommenced or uncertain.
3. **Citations are mandatory.** A fluent answer without evidence is a failed answer.
4. **Plain language without distortion.** Simplicity must not erase legal conditions or exceptions.
5. **Privacy by default.** Collect and retain as little user information as possible.
6. **Political neutrality.** Explain law and legislative processes without electoral persuasion.
7. **Human review for high-risk content.** Sensitive legal topics require stronger controls and escalation.
8. **Open development.** Methods, source policies, evaluation results and corrections should be inspectable.

## Planned architecture

```text
User interface
      |
FastAPI application
      |
Question and risk classifier
      |
Hybrid retrieval
  |             |
Lexical search  Vector search
      |             |
      +------ Reranking ------+
                 |
         Legal-status resolver
                 |
        Ollama language model
                 |
          Citation validator
                 |
        Structured legal answer
```

See [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) for the initial technical design.

## Initial technology choices

- Python 3.12+
- FastAPI
- Ollama
- Qwen or another evaluated multilingual model
- Local multilingual embedding model
- PostgreSQL and pgvector in later phases
- SQLite/FTS or another lightweight local index during prototyping
- Docker Compose
- Pytest, Ruff and mypy

Models are replaceable components. No model should be promoted to production merely because it performs well on general-purpose benchmarks; it must pass the SheriaOpen legal-information evaluation suite.

## Quick start

### 1. Install prerequisites

Install:

- Python 3.12 or later
- Git
- Ollama
- Docker and Docker Compose, optionally

### 2. Clone and configure

```bash
git clone https://github.com/eugene-maina72/sheria-open.git
cd sheria-open
cp .env.example .env
```

Update the clone URL if the repository is created under a different account or organisation.

### 3. Prepare Ollama

```bash
ollama pull qwen3:8b
ollama pull qwen3-embedding:0.6b
```

Model names are configuration defaults, not permanent endorsements. Check each model's own licence before public deployment.

### 4. Run locally with Python

```bash
python -m venv .venv
```

On Linux or macOS:

```bash
source .venv/bin/activate
```

On Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Install and run:

```bash
python -m pip install --upgrade pip
pip install -e ".[dev]"
uvicorn sheriaopen.main:app --reload
```

Open `http://127.0.0.1:8000/health` for liveness. Use
`http://127.0.0.1:8000/ready` to confirm that Ollama is reachable and both
configured models are installed.

### 5. Run with Docker Compose

```bash
docker compose up --build -d
docker compose exec ollama ollama pull qwen3:8b
docker compose exec ollama ollama pull qwen3-embedding:0.6b
```

The Ollama service is kept on the internal Compose network by default. Do not expose the raw Ollama port to the public internet.

## Repository layout

```text
sheriaopen/
├── .github/                 GitHub workflows and contribution templates
├── data/                    Data manifests and local-data instructions
├── docs/                    Architecture, policies and roadmap
├── src/sheriaopen/          Application package
├── tests/                   Automated tests
├── CHANGELOG.md
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── GOVERNANCE.md
├── LICENSE
├── LICENSES/                Multi-licence and third-party notices
├── NOTICE
├── SECURITY.md
├── docker-compose.yml
└── pyproject.toml
```

## Legal-data policy

SheriaOpen will prefer official sources such as Kenya Law, Parliament, the Kenya Gazette and official constitutional commissions, regulators and public bodies. Third-party commentary may support context, but it must not silently replace the primary legal text.

The repository does not claim ownership over official laws, judgments, Bills or third-party materials. Source provenance, official URLs, retrieval dates, version dates and applicable reuse conditions must be preserved.

Read:

- [Data source policy](docs/DATA_SOURCE_POLICY.md)
- [Legal information policy](docs/LEGAL_INFORMATION_POLICY.md)
- [Data directory guidance](data/README.md)

## Contributing

Contributions are welcome from developers, advocates, law students, legal researchers, civic educators, translators, designers, accessibility specialists and ordinary users who identify unclear or incorrect explanations.

Before contributing, read:

- [CONTRIBUTING.md](CONTRIBUTING.md)
- [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)
- [GOVERNANCE.md](GOVERNANCE.md)
- [SECURITY.md](SECURITY.md)

Legal-content changes have additional evidence and review requirements. A pull request that changes a legal explanation must identify the official source, exact provision, document status and verification date.

## Security

Do not open a public issue for a vulnerability that could expose user data, enable source poisoning, bypass citation validation, execute arbitrary requests or expose the Ollama service. Follow [SECURITY.md](SECURITY.md).

## Licensing

- Application code is licensed under **GNU AGPL-3.0-or-later**.
- Original project documentation and curated educational content are intended to be available under **CC BY-SA 4.0**, unless a file states otherwise.
- Official legal texts and third-party materials retain their own legal status, attribution and licence conditions.
- Model weights are governed by their respective model licences.
- The software licence does not grant permission to imply official government, judicial or parliamentary endorsement.

See [LICENSES/README.md](LICENSES/README.md) and [NOTICE](NOTICE).

Before the first public release, use GitHub's licence template or the official GNU/SPDX source to place the complete, unmodified AGPL-3.0-or-later legal text in the root `LICENSE` file.

## Roadmap

The immediate goals are:

1. Build a Constitution-only ingestion pipeline.
2. Implement section-aware lexical and semantic retrieval.
3. Establish a legal-status metadata schema.
4. Create an evaluation set for English and Kiswahili questions.
5. Require structured, citation-backed answers.
6. Conduct legal review before opening public access.

See [docs/ROADMAP.md](docs/ROADMAP.md).

## Citation

Academic and research users can cite the project using [CITATION.cff](CITATION.cff).

## Independence statement

SheriaOpen is an independent open-source project. Unless explicitly stated through a formal partnership, it is not affiliated with, endorsed by or acting on behalf of Kenya Law, the Judiciary, Parliament, IEBC, any ministry, any political party or any other public institution.

## Maintainer

Initial maintainer: [Eugene Maina](https://github.com/eugene-maina72)
