"""Advent of Code 2016 - Day 1 - Part 2.

Find the first location visited twice while following instructions.
"""


def solve(puzzle_input: str) -> int:
    """Solve part 2.

    Approach:
        Track all visited positions while following instructions.
        Instead of jumping to the final position after each instruction,
        track each individual block visited during the walk.
        Return Manhattan distance to the first position visited twice.

    Args:
        puzzle_input: Raw puzzle input string with comma-separated instructions

    Returns:
        The Manhattan distance to the first repeated position

    """
    # Parse instructions
    instructions = [inst.strip() for inst in puzzle_input.strip().split(",")]

    # Directions: North, East, South, West (clockwise)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    direction_idx = 0  # Start facing North
    x, y = 0, 0  # Start at origin

    # Track visited positions
    visited = {(0, 0)}

    for instruction in instructions:
        turn = instruction[0]
        blocks = int(instruction[1:])

        # Update direction
        if turn == "R":
            direction_idx = (direction_idx + 1) % 4
        else:  # turn == "L"
            direction_idx = (direction_idx - 1) % 4

        # Move forward one block at a time, checking for revisits
        dx, dy = directions[direction_idx]
        for _ in range(blocks):
            x += dx
            y += dy
            if (x, y) in visited:
                # Found first repeated position
                return abs(x) + abs(y)
            visited.add((x, y))

    # No position visited twice (shouldn't happen per problem statement)
    return 0


if __name__ == "__main__":
    from aoc.helpers import read_puzzle_input

    answer = solve(read_puzzle_input(2016, 1))
    print(answer)
