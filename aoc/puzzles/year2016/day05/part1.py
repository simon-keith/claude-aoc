"""Advent of Code 2016 - Day 5 - Part 1.

Find password by computing MD5 hashes with incrementing indices.
"""

import hashlib


def solve(puzzle_input: str) -> str:
    """Solve part 1.

    Approach:
        Generate MD5 hashes of door_id + index (starting at 0).
        When a hash starts with five zeroes, the 6th character becomes
        the next password character. Continue until 8 characters found.

    Args:
        puzzle_input: Raw puzzle input string (door ID)

    Returns:
        The 8-character password

    """
    door_id = puzzle_input.strip()
    password = []
    index = 0

    while len(password) < 8:
        hash_input = f"{door_id}{index}"
        hash_result = hashlib.md5(hash_input.encode()).hexdigest()

        if hash_result.startswith("00000"):
            password.append(hash_result[5])

        index += 1

    return "".join(password)


if __name__ == "__main__":
    from aoc.helpers import read_puzzle_input

    answer = solve(read_puzzle_input(2016, 5))
    print(answer)
