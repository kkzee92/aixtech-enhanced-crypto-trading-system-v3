from crypto_trading.strategies import evaluate_strategy

def test_majors_signal():
    features = {"trend_strength": 0.8, "regime": "low_vol"}
    result = evaluate_strategy("majors", features)
    assert result["action"] == "long"
    assert result["confidence"] > 0.5

def test_high_vol_anomaly():
    features = {"anomaly_score": 0.9}
    result = evaluate_strategy("high_vol", features)
    assert result["action"] == "flat"
