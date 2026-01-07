"""Advent of Code 2016 - Day 14 - Part 2.

Same as Part 1 but with key stretching (rehash 2016 times).
"""

import hashlib

from aoc.puzzles.year2016.day14.part1 import find_triplet, has_quintuplet


def get_stretched_hash(salt: str, index: int) -> str:
    """Generate stretched MD5 hash (rehash 2016 times).

    Args:
        salt: Salt string
        index: Index number

    Returns:
        Stretched MD5 hash as hexadecimal string

    """
    hash_str = hashlib.md5(f"{salt}{index}".encode(), usedforsecurity=False).hexdigest()
    for _ in range(2016):
        hash_str = hashlib.md5(hash_str.encode(), usedforsecurity=False).hexdigest()
    return hash_str


def find_64th_key_stretched(salt: str) -> int:
    """Find index that produces the 64th key with key stretching.

    Args:
        salt: Salt string

    Returns:
        Index of 64th key

    """
    keys_found = 0
    index = 0
    # Cache to avoid recomputation
    hash_cache: dict[int, str] = {}

    def get_hash(idx: int) -> str:
        if idx not in hash_cache:
            hash_cache[idx] = get_stretched_hash(salt, idx)
        return hash_cache[idx]

    while keys_found < 64:
        hash_str = get_hash(index)
        triplet = find_triplet(hash_str)

        if triplet:
            for j in range(index + 1, index + 1001):
                next_hash = get_hash(j)
                if has_quintuplet(next_hash, triplet):
                    keys_found += 1
                    if keys_found == 64:
                        return index
                    break

        index += 1

    return -1


def solve(puzzle_input: str) -> str:
    """Solve part 2.

    Approach:
        Same as Part 1 but hash is stretched (rehashed 2016 times).

    Args:
        puzzle_input: Raw puzzle input string (salt)

    Returns:
        Index of 64th key with stretching

    """
    salt = puzzle_input.strip()
    return str(find_64th_key_stretched(salt))


if __name__ == "__main__":
    from aoc.helpers import read_puzzle_input

    answer = solve(read_puzzle_input(2016, 14))
    print(answer)
