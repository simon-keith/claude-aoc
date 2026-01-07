"""Advent of Code 2016 - Day 14 - Part 1.

Find 64th one-time pad key index using MD5 hashes.
"""

import hashlib


def get_hash(salt: str, index: int) -> str:
    """Generate MD5 hash for salt + index.

    Args:
        salt: Salt string
        index: Index number

    Returns:
        MD5 hash as hexadecimal string

    """
    return hashlib.md5(f"{salt}{index}".encode(), usedforsecurity=False).hexdigest()


def find_triplet(hash_str: str) -> str | None:
    """Find first character that appears 3 times in a row.

    Args:
        hash_str: Hash string to search

    Returns:
        Character that appears 3 times, or None

    """
    for i in range(len(hash_str) - 2):
        if hash_str[i] == hash_str[i + 1] == hash_str[i + 2]:
            return hash_str[i]
    return None


def has_quintuplet(hash_str: str, char: str) -> bool:
    """Check if hash contains 5 of the same character in a row.

    Args:
        hash_str: Hash string to search
        char: Character to look for

    Returns:
        True if char appears 5 times in a row

    """
    return char * 5 in hash_str


def find_64th_key(salt: str) -> int:
    """Find index that produces the 64th key.

    Args:
        salt: Salt string

    Returns:
        Index of 64th key

    """
    keys_found = 0
    index = 0

    while keys_found < 64:
        hash_str = get_hash(salt, index)
        triplet = find_triplet(hash_str)

        if triplet:
            # Check next 1000 hashes for quintuplet
            for j in range(index + 1, index + 1001):
                next_hash = get_hash(salt, j)
                if has_quintuplet(next_hash, triplet):
                    keys_found += 1
                    if keys_found == 64:
                        return index
                    break

        index += 1

    return -1


def solve(puzzle_input: str) -> str:
    """Solve part 1.

    Approach:
        Generate MD5 hashes for salt+index. A hash is a key if:
        1. It has 3 same chars in a row
        2. One of next 1000 hashes has that char 5 times in a row

    Args:
        puzzle_input: Raw puzzle input string (salt)

    Returns:
        Index of 64th key

    """
    salt = puzzle_input.strip()
    return str(find_64th_key(salt))


if __name__ == "__main__":
    from aoc.helpers import read_puzzle_input

    answer = solve(read_puzzle_input(2016, 14))
    print(answer)
