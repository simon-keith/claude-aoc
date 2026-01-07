"""Advent of Code 2016 - Day 1 - Part 1.

Calculate Manhattan distance to Easter Bunny HQ following turn/walk instructions.
"""


def solve(puzzle_input: str) -> int:
    """Solve part 1.

    Approach:
        Track position (x, y) and direction (N, E, S, W).
        Parse instructions like "R2, L3" and update position.
        Calculate Manhattan distance from origin.

    Args:
        puzzle_input: Raw puzzle input string with comma-separated instructions

    Returns:
        The Manhattan distance to the final position

    """
    # Parse instructions
    instructions = [inst.strip() for inst in puzzle_input.strip().split(",")]

    # Directions: North, East, South, West (clockwise)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    direction_idx = 0  # Start facing North
    x, y = 0, 0  # Start at origin

    for instruction in instructions:
        turn = instruction[0]
        blocks = int(instruction[1:])

        # Update direction
        if turn == "R":
            direction_idx = (direction_idx + 1) % 4
        else:  # turn == "L"
            direction_idx = (direction_idx - 1) % 4

        # Move forward
        dx, dy = directions[direction_idx]
        x += dx * blocks
        y += dy * blocks

    # Return Manhattan distance
    return abs(x) + abs(y)


if __name__ == "__main__":
    from aoc.helpers import read_puzzle_input

    answer = solve(read_puzzle_input(2016, 1))
    print(answer)
