# Security Policy

## Reporting
Report vulnerabilities via GitHub Security Advisories or private contact.

## Architecture Principles
- Zero Trust: verify every request, least privilege, continuous authentication.
- Defense in depth: multiple layers (ingestion validation, redaction, anomaly detection, audit seals, encryption).
- No secrets in repo: use env vars, GitHub secrets, or external vaults.
- Synthetic data only for development and testing.
- Audit everything: hash-chained logs with multi-hash seals (SHA-256, SHA3-256, BLAKE2b).

## Controls
- Secret scanning (gitleaks-style) in CI.
- Dependency licence allow-list.
- Input validation and redaction of potential keys/seeds/tokens.
- Anomaly detection proxies on data flows and logs.
- Encryption in transit (TLS) and at rest (where applicable).
- No live trading endpoints or private key management.

This is a research system. Real deployments require additional production hardening, penetration testing, and compliance reviews.
