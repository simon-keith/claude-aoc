"""Advent of Code 2016 - Day 15 - Part 2.

Add one more disc and find first time.
"""

from aoc.puzzles.year2016.day15.part1 import parse_discs


def solve(puzzle_input: str) -> str:
    """Solve part 2.

    Approach:
        Add a 7th disc with 11 positions starting at position 0.

    Args:
        puzzle_input: Raw puzzle input string

    Returns:
        First time to press button with extra disc

    """
    lines = puzzle_input.strip().split("\n")
    lines.append("Disc #7 has 11 positions; at time=0, it is at position 0.")
    modified_input = "\n".join(lines)

    discs = parse_discs(modified_input)

    t = 0
    while True:
        success = True
        for disc_num, positions, start_pos in discs:
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
