"""Advent of Code 2016 - Day 20 - Part 1.

Find the lowest IP not blocked by firewall rules.
"""


def parse_ranges(puzzle_input: str) -> list[tuple[int, int]]:
    """Parse the blacklist ranges from input.

    Args:
        puzzle_input: Raw puzzle input string

    Returns:
        List of (start, end) tuples representing blocked ranges

    """
    ranges = []
    for line in puzzle_input.strip().split('\n'):
        start, end = line.split('-')
        ranges.append((int(start), int(end)))
    return ranges


def find_lowest_allowed_ip(ranges: list[tuple[int, int]]) -> int:
    """Find the lowest IP not blocked by any range.

    Args:
        ranges: List of (start, end) tuples representing blocked ranges

    Returns:
        The lowest allowed IP address

    """
    # Sort ranges by start position
    ranges.sort()

    # Track the lowest unblocked IP we're looking for
    lowest_allowed = 0

    for start, end in ranges:
        # If this range starts after our current lowest, we found a gap
        if start > lowest_allowed:
            return lowest_allowed

        # Otherwise, this range might block our current lowest
        # Move past this range if it blocks us
        if end >= lowest_allowed:
            lowest_allowed = end + 1

    return lowest_allowed


def solve(puzzle_input: str) -> str:
    """Solve part 1.

    Approach:
        Parse and sort the blocked IP ranges
        Find the first gap in the ranges

    Args:
        puzzle_input: Raw puzzle input string

    Returns:
        The answer to part 1

    """
    ranges = parse_ranges(puzzle_input)
    return str(find_lowest_allowed_ip(ranges))


if __name__ == "__main__":
    from aoc.helpers import read_puzzle_input

    answer = solve(read_puzzle_input(2016, 20))
    print(answer)
