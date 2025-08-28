def rainbow(text: str) -> str:
    """Return text with rainbow ANSI colors."""
    colors = ["\033[91m", "\033[93m", "\033[92m", "\033[96m", "\033[94m", "\033[95m"]
    reset = "\033[0m"
    return "".join(colors[i % len(colors)] + c for i, c in enumerate(text)) + reset