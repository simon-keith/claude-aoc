"""Advent of Code 2016 - Day 1 - Part 2.

Find the first location visited twice.
"""
from pathlib import Path


def solve() -> int:
    """Solve part 2.

    Approach:
        Track all visited positions as we move
        For each step, record every position along the path (not just endpoints)
        Return Manhattan distance to first position visited twice

    Returns:
        Manhattan distance to first repeated position

    """
    instructions = read_input().split(", ")

    # Starting position and direction
    x, y = 0, 0
    # Direction: 0=North, 1=East, 2=South, 3=West
    direction = 0

    # Direction vectors: North, East, South, West
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    # Track all visited positions
    visited = {(0, 0)}

    for instruction in instructions:
        turn = instruction[0]
        distance = int(instruction[1:])

        # Update direction
        direction = (direction + 1) % 4 if turn == 'R' else (direction - 1) % 4

        # Move forward one block at a time, checking each position
        for _ in range(distance):
            x += dx[direction]
            y += dy[direction]

            # Check if we've been here before
            if (x, y) in visited:
                # Found first repeated location!
                return abs(x) + abs(y)

            visited.add((x, y))

    # Should not reach here based on puzzle description
    return -1


def read_input() -> str:
    """Read and return the input file contents.

    Returns:
        Raw input text with trailing whitespace stripped

    """
    return (Path(__file__).parent / "input.txt").read_text().strip()


if __name__ == "__main__":
    answer = solve()
    print(f"Part 2: {answer}")
