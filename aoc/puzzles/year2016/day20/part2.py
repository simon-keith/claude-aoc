"""Advent of Code 2016 - Day 20 - Part 2.

Count how many IPs are allowed by the firewall.
"""

from aoc.puzzles.year2016.day20 import part1


def count_allowed_ips(ranges: list[tuple[int, int]], max_ip: int = 4294967295) -> int:
    """Count how many IPs are not blocked by any range.

    Args:
        ranges: List of (start, end) tuples representing blocked ranges
        max_ip: Maximum IP address value (default: 4294967295 for 32-bit)

    Returns:
        Number of allowed IPs

    """
    # Sort ranges by start position
    ranges.sort()

    # Merge overlapping ranges
    merged: list[tuple[int, int]] = []
    for start, end in ranges:
        if merged and start <= merged[-1][1] + 1:
            # Overlapping or adjacent - merge
            merged[-1] = (merged[-1][0], max(merged[-1][1], end))
        else:
            # Non-overlapping - add new range
            merged.append((start, end))

    # Count allowed IPs (gaps between merged ranges + before first + after last)
    allowed_count = 0

    # Count IPs before first blocked range
    if merged:
        allowed_count += merged[0][0]

    # Count gaps between blocked ranges
    for i in range(len(merged) - 1):
        gap_start = merged[i][1] + 1
        gap_end = merged[i + 1][0] - 1
        if gap_end >= gap_start:
            allowed_count += gap_end - gap_start + 1

    # Count IPs after last blocked range
    if merged and merged[-1][1] < max_ip:
        allowed_count += max_ip - merged[-1][1]

    # If no ranges, all IPs are allowed
    if not merged:
        allowed_count = max_ip + 1

    return allowed_count


def solve(puzzle_input: str) -> str:
    """Solve part 2.

    Approach:
        Merge overlapping blocked ranges
        Count gaps between merged ranges

    Args:
        puzzle_input: Raw puzzle input string

    Returns:
        The answer to part 2

    """
    ranges = part1.parse_ranges(puzzle_input)
    return str(count_allowed_ips(ranges))


if __name__ == "__main__":
    from aoc.helpers import read_puzzle_input

    answer = solve(read_puzzle_input(2016, 20))
    print(answer)
