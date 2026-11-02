"""Risk engine stubs: adaptive sizing, gates."""

from typing import Dict, Any

def apply_risk_gates(signal: Dict[str, Any], portfolio: Dict[str, Any]) -> Dict[str, Any]:
    """Apply class-specific risk gates and sizing. Paper only."""
    risk_cap = {
        "majors": 0.05,
        "high_vol": 0.005,
        "stables": 0.0,  # alerts only
    }.get(signal.get("class"), 0.02)

    if signal.get("confidence", 0) < 0.4:
        signal["action"] = "hold"
        signal["size"] = 0.0
    else:
        signal["size"] = risk_cap * signal.get("confidence", 0)

    # Drawdown / anomaly kill switch stub
    if portfolio.get("drawdown", 0) > 0.15:
        signal["action"] = "flat"
        signal["size"] = 0.0
        signal["reason"] += " | drawdown gate"

    return signal
