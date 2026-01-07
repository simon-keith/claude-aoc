"""Advent of Code 2016 - Day 5 - Part 2.

Find password using position-based MD5 hash decryption.
"""

import hashlib


def solve(puzzle_input: str) -> str:
    """Solve part 2.

    Approach:
        Generate MD5 hashes of door_id + index (starting at 0).
        When a hash starts with five zeroes:
        - The 6th character is the position (0-7)
        - The 7th character is the value to place at that position
        Use only the first result for each position.

    Args:
        puzzle_input: Raw puzzle input string (door ID)

    Returns:
        The 8-character password

    """
    door_id = puzzle_input.strip()
    password: list[str | None] = [None] * 8
    index = 0
    filled_positions = 0

    while filled_positions < 8:
        hash_input = f"{door_id}{index}"
        hash_result = hashlib.md5(
            hash_input.encode(), usedforsecurity=False
        ).hexdigest()

        if hash_result.startswith("00000"):
            position_char = hash_result[5]
            # Check if position is a valid digit 0-7
            if position_char.isdigit():
                position = int(position_char)
                # Check if position is in valid range and not already filled
                if 0 <= position <= 7 and password[position] is None:
                    password[position] = hash_result[6]
                    filled_positions += 1

        index += 1

    return "".join(c for c in password if c is not None)


if __name__ == "__main__":
    from aoc.helpers import read_puzzle_input

    answer = solve(read_puzzle_input(2016, 5))
    print(answer)
