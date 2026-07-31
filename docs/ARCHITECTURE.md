# Initial architecture

This document describes the target architecture for the first SheriaOpen research prototype. It is intentionally modular so that models, indexes and user interfaces can be replaced independently.

## Components

### API layer

FastAPI exposes health, search and answer endpoints. It validates request size, applies rate limits, records minimal operational metrics and returns structured responses.

### Corpus ingestion

Source-specific adapters retrieve approved official documents, preserve provenance, parse legal structure and create versioned manifests. Parsing should follow articles, sections, subsections, schedules and defined terms rather than arbitrary token windows.

### Retrieval

The first implementation should combine lexical and semantic retrieval. Retrieval results must include document identifiers, provision paths, legal status, effective dates and exact source text.

### Legal-status resolver

The resolver determines whether the relevant instrument is:

- current law;
- a proposed Bill;
- enacted but uncommenced;
- amended;
- repealed;
- revoked;
- expired or spent;
- affected by a judgment; or
- uncertain and requiring review.

Status is determined from structured metadata and official evidence, not from the language model's memory.

### Generation provider

Ollama is the default local inference provider. The application should interact through a provider interface so alternative local or hosted services can be evaluated without rewriting the legal pipeline.

### Citation validator

The validator rejects unsupported citations and checks that cited provisions exist in the retrieved evidence. A generated answer must not introduce a legal instrument absent from the approved context unless explicitly labelled as an unresolved reference.

### Evaluation

Evaluation should measure retrieval recall, citation correctness, status accuracy, faithfulness, completeness of exceptions, plain-language comprehension, Kiswahili quality, latency and refusal behaviour.

## Request flow

```text
request
  -> validation
  -> risk classification
  -> query normalisation
  -> lexical and vector retrieval
  -> reranking
  -> status resolution
  -> structured generation
  -> citation validation
  -> safety and escalation checks
  -> response
```

## Trust boundaries

- Retrieved source text is untrusted input and may contain malicious or irrelevant instructions.
- The raw Ollama endpoint must remain private.
- User-supplied URLs must not be fetched without allow-list and SSRF controls.
- Legal status must not be delegated entirely to generation.
- Logs should avoid storing full sensitive questions by default.

## Initial deployment

The prototype can run on one development machine. A public beta should separate the web/API layer from inference, add a queue and cache, monitor resource use, secure backups and support corpus rollback.
