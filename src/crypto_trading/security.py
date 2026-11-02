"""Security utilities: redaction, multi-hash seals, anomaly stubs."""

import hashlib
import re
from typing import Dict

def redact_sensitive(text: str) -> str:
    """Redact potential private keys, seeds, high-entropy strings."""
    # Simplified patterns for demo
    text = re.sub(r'[1-9A-HJ-NP-Za-km-z]{40,}', '[REDACTED_KEY]', text)
    text = re.sub(r'(0x)?[0-9a-fA-F]{64}', '[REDACTED_HEX]', text)
    return text

def multi_hash_seal(data: str) -> Dict[str, str]:
    """Generate multi-hash seals for audit."""
    encoded = data.encode()
    return {
        "sha256": hashlib.sha256(encoded).hexdigest(),
        "sha3_256": hashlib.sha3_256(encoded).hexdigest(),
        "blake2b": hashlib.blake2b(encoded).hexdigest(),
    }

def anomaly_score(log_entry: str) -> float:
    """Stub anomaly score based on entropy / length."""
    if len(log_entry) > 1000:
        return 0.9
    return 0.05
