import hashlib

def tiny_hash(text: str) -> str:
    """Return a short 6-character hash of the given text."""
    return hashlib.sha256(text.encode()).hexdigest()[:6]