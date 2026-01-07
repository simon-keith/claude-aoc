"""Advent of Code 2016 - Day 19 - Part 1.

Josephus problem - find the last remaining elf.
"""


def find_winner_josephus(num_elves: int) -> int:
    """Find the winner using Josephus problem solution.

    For the Josephus problem with k=2 (every second person eliminated),
    the solution can be computed efficiently using bit manipulation or formula.

    Args:
        num_elves: Number of elves in the circle

    Returns:
        Position of the winning elf (1-indexed)

    """
    # Find the highest power of 2 less than or equal to num_elves
    power_of_2 = 1
    while power_of_2 * 2 <= num_elves:
        power_of_2 *= 2

    return 2 * (num_elves - power_of_2) + 1


def solve(puzzle_input: str) -> str:
    """Solve part 1.

    Approach:
        Use Josephus problem formula for k=2
        Winner = 2 * (n - 2^m) + 1, where 2^m is highest power of 2 <= n

    Args:
        puzzle_input: Raw puzzle input string

    Returns:
        The answer to part 1

    """
    num_elves = int(puzzle_input.strip())
    return str(find_winner_josephus(num_elves))


if __name__ == "__main__":
    from aoc.helpers import read_puzzle_input

    answer = solve(read_puzzle_input(2016, 19))
    print(answer)
