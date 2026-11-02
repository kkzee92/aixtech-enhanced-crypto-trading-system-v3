# AIxTech Enhanced Crypto Trading Information System v3

> **v3 Enhanced** paper-only automated cryptocurrency trading information system with advanced multi-factor adaptive strategies per asset class (regime-aware, multi-timeframe, on-chain proxies), robust zero-trust cyber and data security architecture, and full AI-agent harness principles.
>
> **Research / paper-trading only.** No live order execution, no withdrawal permissions, no storage of exchange secrets or private keys. Not financial, legal, or investment advice.

![Python](https://img.shields.io/badge/python-3.10%2B-blue) ![Licence](https://img.shields.io/badge/licence-MIT-green) ![Mode](https://img.shields.io/badge/execution-paper%20only-orange)

## Overview
Modular framework for crypto trading *information* and paper strategy evaluation, building on [zeekiankok92/aixtech-agent-harness-demo](https://github.com/zeekiankok92/aixtech-agent-harness-demo) and prior kkzee92 versions.

- **Expanded asset classes** with refined multi-factor adaptive strategies (Majors, Large Alts, DeFi, Stables, High-Vol, L2, RWA, Perpetuals, AI-tokens, Meme, GameFi)
- Secure data ingestion (public market data only, synthetic fixtures, redaction)
- Adaptive risk management & position sizing (vol-targeting, correlation, regime filters, anomaly gates, drawdown kill-switches)
- Zero-trust cyber/data security architecture (enhanced redaction, multi-hash seals, anomaly detection stubs, continuous attestation, encryption layers)
- AI-agent safe development (AGENTS.md, disclosure trails, full CI gates)
- Offline-capable simulation and demo hooks

## Quick Start
```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
PYTHONPATH=src python -m crypto_trading demo
PYTHONPATH=src pytest tests/ -q
```

## Architecture
See [docs/architecture.md](docs/architecture.md) and [docs/security-architecture.md](docs/security-architecture.md).

## Asset Class Strategies
See [docs/trading-strategies.md](docs/trading-strategies.md) for detailed multi-factor rules per class.

## Security
[SECURITY.md](SECURITY.md) — Zero Trust, least privilege, secrets via env only, no private keys in code/prompts, synthetic data only.

## AI Agent Rules
See [AGENTS.md](AGENTS.md). Human review required. No production secrets, seeds, or personal data in prompts.

## Licence
[MIT](LICENSE)
