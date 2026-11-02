# Agent Rules for AIxTech Enhanced Crypto Trading System v3

Follow these strictly when assisting with this repository.

## Core Principles
- Paper-only / research. Never suggest or implement live order execution, withdrawals, or private key handling.
- Synthetic fixtures and public open data only. No real user data, exchange API keys, seeds, or mnemonics.
- Human review is mandatory for all changes (Definition of Done = CI green + human sign-off).
- Prefer stdlib where possible; minimize dependencies.

## Security & Data Rules
- Never paste, log, or commit secrets, private keys, seeds, exchange credentials, or high-entropy strings that look like keys.
- Redact sensitive patterns in any generated fixtures or logs.
- Use environment variables or external vaults for any config; never hardcode.
- PDPA-like / data protection: no personal data. Crypto-specific: no wallet addresses that could be linked, no real transaction hashes from production.

## Development Process
- Start from task briefs with acceptance criteria.
- Run local CI gates before proposing changes.
- Include AI-disclosure in commits/PRs.
- Keep changes small, tested, and documented.

## Trading Strategy Guidelines
- Strategies are information/signals only. Document assumptions, limitations, and risk.
- Use multi-factor, adaptive rules. Include regime filters, risk gates.
- Backtest on synthetic or public historical data only.
- Emphasize risk management over return maximization.

See harness/ for templates and checklists.
