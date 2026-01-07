"""Advent of Code 2016 - Day 4 - Part 1.

Validate encrypted room names using checksums.
"""

import re
from collections import Counter


def parse_room(room: str) -> tuple[str, int, str]:
    """Parse a room string into its components.

    Args:
        room: Room string like "aaaaa-bbb-z-y-x-123[abxyz]"

    Returns:
        Tuple of (encrypted_name, sector_id, checksum)

    """
    # Match pattern: letters-and-dashes, number, [checksum]
    match = re.match(r"^([a-z-]+)-(\d+)\[([a-z]+)\]$", room)
    if not match:
        raise ValueError(f"Invalid room format: {room}")

    encrypted_name = match.group(1)
    sector_id = int(match.group(2))
    checksum = match.group(3)

    return encrypted_name, sector_id, checksum


def compute_checksum(encrypted_name: str) -> str:
    """Compute the expected checksum for an encrypted name.

    The checksum is the five most common letters, ordered by:
    1. Frequency (descending)
    2. Alphabetical order (ascending) for ties

    Args:
        encrypted_name: Encrypted name with dashes

    Returns:
        Five-character checksum string

    """
    # Count letters (ignore dashes)
    letter_counts = Counter(encrypted_name.replace("-", ""))

    # Sort by frequency (descending), then alphabetically (ascending)
    sorted_letters = sorted(letter_counts.items(), key=lambda x: (-x[1], x[0]))

    # Take first 5 letters
    return "".join(letter for letter, _ in sorted_letters[:5])


def is_real_room(room: str) -> bool:
    """Check if a room is real based on its checksum.

    Args:
        room: Room string like "aaaaa-bbb-z-y-x-123[abxyz]"

    Returns:
        True if the checksum matches the expected value

    """
    encrypted_name, _, checksum = parse_room(room)
    expected_checksum = compute_checksum(encrypted_name)
    return checksum == expected_checksum


def solve(puzzle_input: str) -> int:
    """Solve part 1.

    Approach:
        Parse each room to extract encrypted name, sector ID, and checksum.
        Compute expected checksum by counting letter frequencies.
        Sum sector IDs of rooms with valid checksums.

    Args:
        puzzle_input: Raw puzzle input string with one room per line

    Returns:
        The sum of sector IDs for real rooms

    """
    sector_sum = 0

    for line in puzzle_input.strip().split("\n"):
        if is_real_room(line):
            _, sector_id, _ = parse_room(line)
            sector_sum += sector_id

    return sector_sum


if __name__ == "__main__":
    from aoc.helpers import read_puzzle_input

    answer = solve(read_puzzle_input(2016, 4))
    print(answer)
