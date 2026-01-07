"""Advent of Code 2016 - Day 12 - Part 2.

Execute assembunny code with register c initialized to 1.
"""

from aoc.puzzles.year2016.day12.part1 import execute


def solve(puzzle_input: str) -> str:
    """Solve part 2.

    Approach:
        Same as Part 1, but initialize register c to 1.

    Args:
        puzzle_input: Raw puzzle input string

    Returns:
        Value in register a after execution

    """
    instructions = puzzle_input.strip().split("\n")
    registers = {"a": 0, "b": 0, "c": 1, "d": 0}

    result = execute(instructions, registers)
    return str(result["a"])


if __name__ == "__main__":
    from aoc.helpers import read_puzzle_input

    answer = solve(read_puzzle_input(2016, 12))
    print(answer)
