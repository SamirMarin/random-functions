def emojify(sentence: str) -> str:
    """Replace some words with emojis."""
    mapping = {"love": "❤️", "cat": "🐱", "dog": "🐶", "fire": "🔥", "rocket": "🚀"}
    return " ".join(mapping.get(w, w) for w in sentence.split())