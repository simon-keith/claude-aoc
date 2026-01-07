"""Advent of Code 2016 - Day 6 - Part 1.

Decode error-corrected message by finding most frequent character per column.
"""

from collections import Counter


def solve(puzzle_input: str) -> str:
    """Solve part 1.

    Approach:
        Parse lines into columns, then for each column find the most
        common character. Combine these characters to form the message.

    Args:
        puzzle_input: Raw puzzle input string

    Returns:
        The error-corrected message

    """
    lines = puzzle_input.strip().split("\n")
    if not lines:
        return ""

    message_length = len(lines[0])
    message = []

    # For each column position
    for col_idx in range(message_length):
        # Count characters in this column
        column_chars = [line[col_idx] for line in lines]
        counter = Counter(column_chars)
        # Get the most common character
        most_common_char = counter.most_common(1)[0][0]
        message.append(most_common_char)

    return "".join(message)


if __name__ == "__main__":
    from aoc.helpers import read_puzzle_input

    answer = solve(read_puzzle_input(2016, 6))
    print(answer)
