# Data directory

This directory stores manifests, schemas and small public test fixtures. Large legal corpora, private user material and generated indexes should not be committed to Git.

## Intended layout

```text
data/
├── manifests/       Source URLs, versions, hashes and retrieval metadata
├── schemas/         Document and legal-status schemas
├── fixtures/        Small, reviewable test documents
├── raw/             Local downloads; ignored by Git
├── processed/       Parsed documents; ignored by Git
├── indexes/         Search and vector indexes; ignored by Git
└── cache/           Temporary retrieval and answer cache; ignored by Git
```

## Required provenance fields

Every ingested official document should retain:

- canonical title;
- document type;
- official citation or number;
- issuing body;
- official source URL;
- publication, assent and commencement dates where applicable;
- effective-from and effective-to dates where applicable;
- current legal status;
- amendment or repeal relationships;
- retrieval timestamp;
- last verification timestamp;
- content checksum; and
- parser version.

## Prohibited material

Do not commit:

- private case files;
- personally identifying user questions;
- access tokens or session cookies;
- documents acquired by bypassing access controls;
- proprietary legal databases without permission; or
- model-generated legal summaries presented as official source data.

## Redistribution

Official and third-party documents are not relicensed by SheriaOpen. Check source-specific terms before publishing a data release.
