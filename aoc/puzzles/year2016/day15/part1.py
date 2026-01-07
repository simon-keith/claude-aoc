"""Advent of Code 2016 - Day 15 - Part 1.

Find first time to press button so capsule passes through all discs.
"""

import re


def parse_discs(puzzle_input: str) -> list[tuple[int, int, int]]:
    """Parse disc configuration.

    Args:
        puzzle_input: Raw puzzle input string

    Returns:
        List of (disc_num, positions, start_pos) tuples

    """
    discs = []
    for line in puzzle_input.strip().split("\n"):
        match = re.match(
            r"Disc #(\d+) has (\d+) positions; at time=0, it is at position (\d+).",
            line,
        )
        if match:
            disc_num = int(match.group(1))
            positions = int(match.group(2))
            start_pos = int(match.group(3))
            discs.append((disc_num, positions, start_pos))
    return discs


def solve(puzzle_input: str) -> str:
    """Solve part 1.

    Approach:
        For capsule to pass, each disc must be at position 0 when
        capsule reaches it. Disc i is reached at time t+i.
        Find minimum t where (start_pos + t + disc_num) % positions == 0
        for all discs.

    Args:
        puzzle_input: Raw puzzle input string

    Returns:
        First time to press button

    """
    discs = parse_discs(puzzle_input)

    t = 0
    while True:
        success = True
        for disc_num, positions, start_pos in discs:
            # Capsule reaches this disc at time t + disc_num
            disc_position = (start_pos + t + disc_num) % positions
            if disc_position != 0:
                success = False
                break

        if success:
            return str(t)

        t += 1


if __name__ == "__main__":
    from aoc.helpers import read_puzzle_input

    answer = solve(read_puzzle_input(2016, 15))
    print(answer)
