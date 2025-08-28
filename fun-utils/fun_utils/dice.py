import random

def roll_dice(sides=6) -> int:
    """Roll a dice with N sides and return the result."""
    return random.randint(1, sides)