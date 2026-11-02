# Security Architecture (v3)

## Zero-Trust Model
- Verify explicitly, least privilege access, assume breach.
- Continuous attestation of data sources and code integrity.

## Layers
1. **Ingestion**: Schema validation, range checks, redaction of high-entropy strings, potential private key / seed patterns, API key formats.
2. **Processing**: Isolated feature computation, no external network in core path unless explicitly injected and audited.
3. **Strategies & Risk**: Deterministic rules, no side effects that could lead to execution.
4. **Audit**: Immutable hash-chained logs. Multi-hash seals (SHA-256 + SHA3-256 + BLAKE2b). Anomaly detection on log volume, entropy, residual patterns.
5. **Encryption**: TLS for any external calls; AES-GCM style stubs for sensitive local data (if any). Secrets never at rest in plain text in the system.

## Controls
- CI secret scanning (gitleaks-style).
- Licence allow-list.
- PDPA-style guard adapted for crypto secrets (no seeds, mnemonics, private keys, exchange credentials).
- Dependency scanning.
- Human review mandatory.

## Redaction Patterns (examples)
- High-entropy base58 / hex strings longer than threshold
- Common key prefixes (e.g., private key formats)
- Seed phrase word sequences

See `src/crypto_trading/security.py` for implementation stubs.
