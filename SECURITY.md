# Security policy

SheriaOpen handles legal questions and may process sensitive information. Security and privacy reports are taken seriously even during early development.

## Supported versions

Before the first stable release, only the latest commit on the default branch is supported. After versioned releases begin, this table will be updated.

| Version | Supported |
|---|---|
| Development branch | Yes |
| Older snapshots and forks | No guarantee |

## Reporting a vulnerability

Do not open a public issue for a vulnerability.

Use GitHub's private vulnerability reporting or a private security advisory when available. Before public launch, configure and publish a dedicated security contact address.

Include:

- affected version or commit;
- reproduction steps;
- potential impact;
- proof-of-concept material, where safe;
- suggested mitigation, if known; and
- whether the issue has been disclosed elsewhere.

Do not include real users' legal questions, credentials, private documents or unnecessary personal data.

## Security issues of particular interest

Please report:

- remote code execution or command injection;
- server-side request forgery;
- authentication or authorisation bypass;
- exposure of environment variables, API keys or database credentials;
- public exposure of the Ollama service;
- prompt injection that changes source policy or disables citation checks;
- malicious content inserted into the legal corpus;
- citation fabrication or source substitution;
- poisoning of embeddings, indexes or legal-status metadata;
- cross-user data leakage;
- retention of sensitive prompts contrary to policy;
- unsafe file upload or document parsing;
- dependency or container vulnerabilities with a practical attack path; and
- denial-of-service weaknesses that could create unreasonable inference costs.

## Response targets

These are targets, not contractual guarantees:

- acknowledgement within 3 working days;
- initial triage within 7 working days;
- progress update at least every 14 days while unresolved; and
- coordinated disclosure after a fix or agreed mitigation is available.

## Safe-harbour intent

Good-faith research that avoids privacy violations, service disruption, data destruction and unnecessary access will not be treated as malicious. Stop testing and report immediately if you encounter personal data or gain access beyond what is needed to demonstrate the issue.

## Deployment baseline

Public deployments should:

- keep Ollama on a private network;
- enforce request-size and output-token limits;
- use timeouts and concurrency controls;
- validate all external URLs and redirects;
- sandbox parsers and ingestion jobs;
- use least-privilege credentials;
- encrypt network traffic;
- maintain tested backups;
- avoid logging full sensitive prompts by default; and
- support rapid corpus rollback when a source is compromised.

## Legal emergencies

The security channel is not an emergency legal-support service. Users facing immediate danger or a legal deadline should contact an appropriate emergency service, legal-aid provider or qualified advocate.
