"""Advent of Code 2016 - Day 1 - Part 1.

No Time for a Taxicab: Calculate Manhattan distance to destination.
"""
from pathlib import Path


def solve() -> int:
    """Solve part 1.

    Approach:
        Track position (x, y) and facing direction
        Parse each instruction (turn + distance)
        Update direction based on turn (L/R)
        Move forward in current direction
        Return Manhattan distance from origin

    Returns:
        Manhattan distance to final position

    """
    instructions = read_input().split(", ")

    # Starting position and direction
    x, y = 0, 0
    # Direction: 0=North, 1=East, 2=South, 3=West
    direction = 0

    # Direction vectors: North, East, South, West
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    for instruction in instructions:
        turn = instruction[0]
        distance = int(instruction[1:])

        # Update direction
        direction = (direction + 1) % 4 if turn == 'R' else (direction - 1) % 4

        # Move forward
        x += dx[direction] * distance
        y += dy[direction] * distance

    # Manhattan distance
    return abs(x) + abs(y)


def read_input() -> str:
    """Read and return the input file contents.

    Returns:
        Raw input text with trailing whitespace stripped

    """
    return (Path(__file__).parent / "input.txt").read_text().strip()


if __name__ == "__main__":
    answer = solve()
    print(f"Part 1: {answer}")
