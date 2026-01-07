"""Advent of Code 2016 - Day 7 - Part 2.

Count IPv7 addresses that support SSL.
"""

import re


def find_abas(text: str) -> set[str]:
    """Find all ABA patterns in text.

    An ABA is a 3-character sequence like xyx or aba where
    the first and third characters are the same but different
    from the middle character.

    Args:
        text: String to search

    Returns:
        Set of ABA patterns found

    """
    abas = set()
    for i in range(len(text) - 2):
        if text[i] == text[i + 2] and text[i] != text[i + 1]:
            abas.add(text[i : i + 3])
    return abas


def aba_to_bab(aba: str) -> str:
    """Convert an ABA pattern to its corresponding BAB pattern.

    Args:
        aba: ABA pattern (e.g., "xyx")

    Returns:
        Corresponding BAB pattern (e.g., "yxy")

    """
    return aba[1] + aba[0] + aba[1]


def supports_ssl(ip_address: str) -> bool:
    """Check if an IPv7 address supports SSL.

    An IP supports SSL if it has an ABA outside brackets
    and the corresponding BAB inside brackets.

    Args:
        ip_address: IPv7 address string

    Returns:
        True if the address supports SSL

    """
    # Split into parts inside and outside brackets
    parts_outside = re.split(r"\[.*?\]", ip_address)
    parts_inside = re.findall(r"\[([^\]]+)\]", ip_address)

    # Find all ABAs outside brackets
    abas_outside = set()
    for part in parts_outside:
        abas_outside.update(find_abas(part))

    # Find all ABAs inside brackets (which are BABs from our perspective)
    abas_inside = set()
    for part in parts_inside:
        abas_inside.update(find_abas(part))

    # Check if any ABA outside has its corresponding BAB inside
    for aba in abas_outside:
        bab = aba_to_bab(aba)
        if bab in abas_inside:
            return True

    return False


def solve(puzzle_input: str) -> str:
    """Solve part 2.

    Approach:
        For each IP address, check if it supports SSL by:
        1. Finding all ABA patterns outside brackets
        2. Finding all ABA patterns inside brackets
        3. Checking if any ABA outside has a corresponding BAB inside

    Args:
        puzzle_input: Raw puzzle input string

    Returns:
        The number of IPs that support SSL

    """
    ip_addresses = puzzle_input.strip().split("\n")
    count = sum(1 for ip in ip_addresses if supports_ssl(ip))
    return str(count)


if __name__ == "__main__":
    from aoc.helpers import read_puzzle_input

    answer = solve(read_puzzle_input(2016, 7))
    print(answer)
