"""Advent of Code 2016 - Day 7 - Part 1.

Count IPv7 addresses that support TLS.
"""

import re


def has_abba(text: str) -> bool:
    """Check if text contains an ABBA pattern.

    An ABBA is a 4-character sequence like xyyx or abba where
    the first two characters are different but reversed in the second half.

    Args:
        text: String to check

    Returns:
        True if text contains an ABBA pattern

    """
    for i in range(len(text) - 3):
        # Check if positions form ABBA pattern
        if (
            text[i] == text[i + 3]
            and text[i + 1] == text[i + 2]
            and text[i] != text[i + 1]
        ):
            return True
    return False


def supports_tls(ip_address: str) -> bool:
    """Check if an IPv7 address supports TLS.

    An IP supports TLS if:
    - It has an ABBA outside square brackets
    - It does NOT have an ABBA inside square brackets

    Args:
        ip_address: IPv7 address string

    Returns:
        True if the address supports TLS

    """
    # Split into parts inside and outside brackets
    parts_outside = re.split(r"\[.*?\]", ip_address)
    parts_inside = re.findall(r"\[([^\]]+)\]", ip_address)

    # Check if any ABBA exists inside brackets (disqualifies)
    for part in parts_inside:
        if has_abba(part):
            return False

    # Check if any ABBA exists outside brackets (qualifies)
    for part in parts_outside:
        if has_abba(part):
            return True

    return False


def solve(puzzle_input: str) -> str:
    """Solve part 1.

    Approach:
        For each IP address, check if it supports TLS by:
        1. Parsing parts inside/outside brackets
        2. Checking for ABBA patterns in each part
        3. Ensuring ABBA exists outside but not inside brackets

    Args:
        puzzle_input: Raw puzzle input string

    Returns:
        The number of IPs that support TLS

    """
    ip_addresses = puzzle_input.strip().split("\n")
    count = sum(1 for ip in ip_addresses if supports_tls(ip))
    return str(count)


if __name__ == "__main__":
    from aoc.helpers import read_puzzle_input

    answer = solve(read_puzzle_input(2016, 7))
    print(answer)
