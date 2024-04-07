import random
import time
from enum import Enum

class Move(Enum):
    TWIRL = 1
    LEAP = 2
    SPIN = 3


def random_moves_generator(n=3):
    """
    Generates a sequence of random moves.

    Args:
        n (int): The length of each move sequence. Defaults to 3.

    Yields:
        tuple: A tuple representing a random move sequence of length n.

    """
    moves = list(Move)
    while True:
        yield tuple(random.choice(moves) for _ in range(n))
        time.sleep(1)

def get_magical_effect(moves):
    """
    Determines the magical effect based on the given sequence of moves.

    Args:
        moves (tuple): A tuple of Move objects representing the sequence of moves.

    Returns:
        str: The magical effect corresponding to the given sequence of moves.

    """
    if all(move == Move.TWIRL for move in moves):
        return "Fireflies light up the forest"
    elif moves == (Move.LEAP, Move.SPIN):
        return "Gentle rain starts falling"
    elif moves == (Move.SPIN, Move.LEAP):
        return "A rainbow appears in the sky"
    elif moves == (Move.TWIRL, Move.LEAP):
        return "A gust of wind rustles the leaves"
    elif moves == (Move.LEAP, Move.TWIRL):
        return "The forest floor blooms with flowers"
    elif moves == (Move.SPIN, Move.TWIRL):
        return "A chorus of birds begins to sing"
    elif moves == (Move.TWIRL, Move.SPIN):
        return "The trees sway in rhythm"
    elif moves == (Move.LEAP, Move.SPIN, Move.TWIRL):
        return "A beautiful sunset paints the sky"
    elif moves == (Move.TWIRL, Move.LEAP, Move.SPIN):
        return "The forest glows with a soft light"
    elif moves == (Move.SPIN, Move.TWIRL, Move.LEAP):
        return "A gentle snow begins to fall"
    else:
        return "No magical effect"

def update_forest_state(effect):
    if effect == "Fireflies light up the forest":
        return "Forest is bright"
    elif effect == "Gentle rain starts falling":
        return "Forest is damp"
    elif effect == "A rainbow appears in the sky":
        return "Forest is colorful"
    elif effect == "A gust of wind rustles the leaves":
        return "Forest is windy"
    elif effect == "The forest floor blooms with flowers":
        return "Forest is blooming"
    elif effect == "A chorus of birds begins to sing":
        return "Forest is noisy"
    elif effect == "The trees sway in rhythm":
        return "Forest is swaying"
    elif effect == "A beautiful sunset paints the sky":
        return "Forest is glowing"
    elif effect == "The forest glows with a soft light":
        return "Forest is illuminated"
    elif effect == "A gentle snow begins to fall":
        return "Forest is snowy"
    else:
        return "Forest is normal"

def simulate_dance():
    # lox_moves = [Move.TWIRL, Move.LEAP, Move.SPIN, Move.TWIRL, Move.LEAP]
    # drako_moves = [Move.SPIN, Move.TWIRL, Move.LEAP, Move.LEAP, Move.SPIN]
    for i, moves in enumerate(random_moves_generator(n=2)):
        effect = get_magical_effect(moves)
        print(f"Creature moves: {', '.join(move.name for move in moves)}, which caused the following effect: {effect}")
        forest_state = update_forest_state(effect)
        print(f"Sequence {i+1}: {forest_state}")

if __name__ == "__main__":
    simulate_dance()
    