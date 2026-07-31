# Data source policy

## Purpose

SheriaOpen answers should be grounded in sources that users can inspect and verify. This policy defines the order in which sources are trusted.

## Source hierarchy

### Tier 1: primary official legal sources

Examples include official legislation, the Constitution, Bills, Gazette notices, commencement instruments, subsidiary legislation, parliamentary records and judicial decisions published by the responsible public institution or an authorised official legal publisher.

Tier 1 sources establish legal text and formal status.

### Tier 2: official explanatory sources

Guidance from constitutional commissions, regulators, ministries, Parliament, the Judiciary and other public bodies may explain implementation. Such guidance must not be presented as though it amends the governing legal text.

### Tier 3: reputable secondary analysis

Academic publications, established legal organisations and expert commentary may help identify context, debate or interpretation. They must be labelled as secondary and should not be the only source for a claim about current legal status.

### Tier 4: public claims and media

News, speeches, political statements, blogs and social-media content may be analysed as claims. They are not authoritative legal sources and must be verified against higher-tier evidence.

## Ingestion requirements

Each source adapter should:

- use a documented and respectful retrieval method;
- preserve the official URL and metadata;
- record retrieval time and checksum;
- detect material changes;
- avoid bypassing authentication or technical restrictions;
- comply with applicable source terms; and
- fail visibly rather than silently using stale material.

## Staleness

Answers should show a last-verified date. High-change sources such as Bills and Gazette notices require more frequent checks than stable constitutional provisions.

## Conflicts

When official sources appear inconsistent, SheriaOpen should state the conflict, cite both sources and route the item for review. The language model must not silently choose the version that produces the most convenient answer.

## Corrections and takedowns

A source may be disabled or rolled back when it is corrupted, misparsed, unlawfully acquired, incorrectly attributed or superseded. Material corrections should be recorded.
