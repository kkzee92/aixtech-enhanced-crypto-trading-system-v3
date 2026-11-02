from crypto_trading.security import redact_sensitive, multi_hash_seal

def test_redact():
    text = "private key 5HueCGU8rMjxEXxiPuD5BDku4MkFqeZyd4dZ1jvhTVqvbTLvyTJ"
    redacted = redact_sensitive(text)
    assert "[REDACTED" in redacted

def test_seal():
    seals = multi_hash_seal("test data")
    assert "sha256" in seals
    assert len(seals["sha256"]) == 64
