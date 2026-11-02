# Trading Strategies per Asset Class (v3 Enhanced)

All strategies are paper-only information signals. They use multi-factor adaptive rules with regime awareness. Assumptions documented; not financial advice.

## Common Building Blocks
- Trend: Adaptive EMA / Supertrend / ATR channels
- Momentum: RSI, rate-of-change
- Volatility: ATR percentile, regime clustering
- Volume / Flow: relative volume, funding rate, open interest change
- Relative: strength vs benchmark (BTC/ETH), correlation filters
- On-chain / Activity proxies (where available): TVL change, fee revenue, active addresses (synthetic)
- Risk filters: anomaly score, drawdown, time-stop

## Asset Classes

| Class | Examples | Key Factors | Risk Profile | Notes |
|-------|----------|-------------|--------------|-------|
| Majors | BTC, ETH | Adaptive EMA + ATR + funding/OI + vol regime | Medium | Core trend following with mean-reversion overlay in high vol |
| Large Alts | SOL, BNB, ADA | Relative strength + breakout + correlation to BTC | Medium-High | Filter when BTC dominance rising |
| DeFi | UNI, AAVE, LINK | Price + TVL/fee growth + isolation + risk-parity | High | Protocol-specific risk gates |
| Stables | USDT, USDC | Peg deviation + volume + netflow proxies | Low (alert only) | Alert on depeg > threshold |
| High Vol / Meme | DOGE, PEPE, new | Strict 0.5% risk, time stops, anomaly filter, volume burst | Very High | Tight stops, short holds |
| L2 | ARB, OP | Relative strength vs ETH + adaptive MTF | Medium | Ecosystem narrative filters |
| RWA | Tokenized assets | Slow multi-scale + gap/anomaly halt | Low-Medium | Conservative, event-driven |
| Perpetuals | Perp markets | Funding carry + contained drift + OI change | Medium | Funding arbitrage signals |
| AI-tokens | FET, AGIX, etc. | Hybrid burst + activity proxy + divergence | High | Narrative + technical |
| GameFi | AXS, SAND, etc. | Activity + price relative + volume | High | Seasonal / event aware |

Detailed rule stubs are in `src/crypto_trading/strategies.py`.

Enhancements in v3: better regime detection, multi-timeframe confluence, expanded on-chain proxies, adaptive parameter selection based on recent volatility clustering.
