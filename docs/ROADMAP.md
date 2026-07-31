# Development roadmap

## Phase 0: repository and governance

- Establish repository policies and licences.
- Configure automated quality checks.
- Define legal-status and source metadata schemas.
- Recruit initial technical and legal reviewers.

## Phase 1: Constitution-only prototype

- Ingest the Constitution with article-level structure.
- Build lexical retrieval.
- Add multilingual embeddings and hybrid retrieval.
- Create an English evaluation set.
- Return exact article citations without generation.

**Release gate:** correct provision appears in the top retrieval results for the approved benchmark.

## Phase 2: controlled RAG answers

- Integrate Ollama through a provider interface.
- Add structured legal-answer schemas.
- Validate every generated citation.
- Implement uncertainty and refusal behaviour.
- Add answer caching tied to corpus and prompt versions.

**Release gate:** no invented document or provision in the release evaluation set.

## Phase 3: Kiswahili and usability

- Develop reviewed Kiswahili terminology.
- Add mobile-first interface and accessibility testing.
- Test user comprehension before and after answers.
- Add correction and feedback workflows.

**Release gate:** domain-reviewed English and Kiswahili quality meets agreed thresholds.

## Phase 4: selected Acts

- Add a controlled set of high-demand Acts.
- Implement amendment, commencement and repeal metadata.
- Add cross-document retrieval.
- Expand high-risk escalation rules.

**Release gate:** legal status is correct for all documents in the release corpus.

## Phase 5: Bills and legislative tracking

- Add National Assembly and Senate Bill tracking.
- Compare proposed amendments with current law.
- Add source-change monitoring and alerts.
- Publish a public corrections and status-change log.

**Release gate:** the system consistently distinguishes proposals from binding law.

## Phase 6: public beta

- Add rate limiting, monitoring, backups and queueing.
- Conduct security, privacy and legal review.
- Publish evaluation results and known limitations.
- Start a controlled partner pilot.

**Release gate:** maintainers and domain reviewers formally approve public access.
