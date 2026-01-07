"""Advent of Code 2016 - Day 16 - Part 2.

Generate data using dragon curve for larger disk and compute checksum.
"""

from aoc.puzzles.year2016.day16 import part1


def solve(puzzle_input: str) -> str:
    """Solve part 2.

    Approach:
        Reuse part1 logic with larger disk length (35651584)

    Args:
        puzzle_input: Raw puzzle input string

    Returns:
        The answer to part 2

    """
    return part1.solve(puzzle_input, disk_length=35651584)


if __name__ == "__main__":
    from aoc.helpers import read_puzzle_input

    answer = solve(read_puzzle_input(2016, 16))
    print(answer)
