"""Advent of Code 2016 - Day 19 - Part 2.

Josephus variant - steal from across the circle.
"""


def find_winner_across(num_elves: int) -> int:
    """Find the winner when stealing from across the circle.

    This is a variant of the Josephus problem where we eliminate
    the elf directly across (at position n//2) each time.

    There's a mathematical pattern:
    - If n is a power of 3, winner is n
    - Otherwise, find the highest power of 3 below n (call it p)
    - If n <= 2*p, winner = n - p
    - If n > 2*p, winner = 2*n - 3*p

    Args:
        num_elves: Number of elves in the circle

    Returns:
        Position of the winning elf (1-indexed)

    """
    # Find the highest power of 3 less than or equal to num_elves
    power_of_3 = 1
    while power_of_3 * 3 <= num_elves:
        power_of_3 *= 3

    if num_elves == power_of_3:
        return num_elves

    if num_elves <= 2 * power_of_3:
        return num_elves - power_of_3
    return 2 * num_elves - 3 * power_of_3


def solve(puzzle_input: str) -> str:
    """Solve part 2.

    Approach:
        Use mathematical pattern for Josephus variant
        where elimination happens across the circle

    Args:
        puzzle_input: Raw puzzle input string

    Returns:
        The answer to part 2

    """
    num_elves = int(puzzle_input.strip())
    return str(find_winner_across(num_elves))


if __name__ == "__main__":
    from aoc.helpers import read_puzzle_input

    answer = solve(read_puzzle_input(2016, 19))
    print(answer)
