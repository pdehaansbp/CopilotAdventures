from enum import Enum


class Move(Enum):
    TWIRL = 'Twirl'
    LEAP = 'Leap'
    SPIN = 'Spin'


def get_magical_effect(moves: tuple[Move, ...]) -> str:
    if all(move == Move.TWIRL for move in moves):
        return "Fireflies light up the forest"
    elif moves == (Move.LEAP, Move.SPIN):
        return "Gentle rain starts falling"
    elif moves == (Move.SPIN, Move.LEAP):
        return "A rainbow appears in the sky"
    else:
        return "No magical effect"

# Example usage
def main():
    creature1_move = Move.SPIN
    creature2_move = Move.LEAP
    effect = get_magical_effect((creature1_move, creature2_move))
    print(effect)


if __name__ == "__main__":
    main()
