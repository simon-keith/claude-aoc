"""Advent of Code 2016 - Day 11 - Part 2.

Add 4 extra items and find minimum steps.
"""

from aoc.puzzles.year2016.day11.part1 import solve as solve_part1


def solve(puzzle_input: str) -> str:
    """Solve part 2.

    Approach:
        Add elerium and dilithium generators/chips to first floor,
        then use the same BFS algorithm as Part 1.

    Args:
        puzzle_input: Raw puzzle input string

    Returns:
        Minimum number of steps with extra items

    """
    # Modify the first line to include the extra items
    lines = puzzle_input.strip().split("\n")
    first_line = lines[0]

    # Add the extra items to the first floor
    extra_items = (
        "an elerium generator, an elerium-compatible microchip, "
        "a dilithium generator, and a dilithium-compatible microchip"
    )

    # Insert before the period at the end
    if first_line.endswith("."):
        first_line = first_line[:-1] + ", " + extra_items + "."
    else:
        first_line = first_line + ", " + extra_items

    lines[0] = first_line
    modified_input = "\n".join(lines)

    return solve_part1(modified_input)


if __name__ == "__main__":
    from aoc.helpers import read_puzzle_input

    answer = solve(read_puzzle_input(2016, 11))
    print(answer)
