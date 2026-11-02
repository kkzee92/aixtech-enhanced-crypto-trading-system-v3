"""Feature engineering stubs for multi-factor adaptive strategies."""

from typing import Dict, Any, List

def compute_features(prices: List[float], volumes: List[float], extras: Dict[str, Any] = None) -> Dict[str, Any]:
    """Compute proxy features: trend, vol, volume, regime. Offline / synthetic friendly."""
    if not prices:
        return {"trend_strength": 0.0, "vol": 0.0, "regime": "unknown"}

    # Simple proxies (expandable)
    returns = [(prices[i] - prices[i-1]) / prices[i-1] for i in range(1, len(prices))] if len(prices) > 1 else [0]
    vol = sum(abs(r) for r in returns[-10:]) / max(len(returns[-10:]), 1) if returns else 0
    trend = (prices[-1] - prices[0]) / prices[0] if prices else 0
    regime = "high_vol" if vol > 0.05 else "low_vol" if vol < 0.02 else "neutral"

    return {
        "trend_strength": min(max(trend * 5, -1), 1),  # normalized proxy
        "volatility": vol,
        "regime": regime,
        "volume_ratio": 1.0,  # stub
        "anomaly_score": 0.1,  # stub
        **(extras or {})
    }
