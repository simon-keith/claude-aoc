"""Advent of Code 2016 - Day 18 - Part 2.

Count safe tiles with many more rows.
"""

from aoc.puzzles.year2016.day18 import part1


def solve(puzzle_input: str) -> str:
    """Solve part 2.

    Approach:
        Reuse part1 logic with 400000 rows

    Args:
        puzzle_input: Raw puzzle input string

    Returns:
        The answer to part 2

    """
    return part1.solve(puzzle_input, total_rows=400000)


if __name__ == "__main__":
    from aoc.helpers import read_puzzle_input

    answer = solve(read_puzzle_input(2016, 18))
    print(answer)
