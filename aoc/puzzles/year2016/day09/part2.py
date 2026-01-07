"""Advent of Code 2016 - Day 9 - Part 2.

Calculate decompressed length with recursive marker processing.
"""


def decompress_length_v2(compressed: str) -> int:
    """Calculate decompressed length with recursive marker processing.

    Approach:
        Parse the compressed string recursively. When encountering
        a marker, extract the specified substring and recursively
        calculate its decompressed length, then multiply by the
        repeat count.

    Args:
        compressed: Compressed string

    Returns:
        Decompressed length

    """
    # Remove whitespace
    compressed = "".join(compressed.split())

    length = 0
    i = 0

    while i < len(compressed):
        if compressed[i] == "(":
            # Find the closing parenthesis
            close_idx = compressed.index(")", i)
            marker = compressed[i + 1 : close_idx]

            # Parse marker
            char_count, repeat_count = map(int, marker.split("x"))

            # Skip past the marker
            i = close_idx + 1

            # Extract the substring to be repeated
            substring = compressed[i : i + char_count]

            # Recursively calculate the decompressed length of the substring
            substring_length = decompress_length_v2(substring)

            # Add the total length (substring length * repeat count)
            length += substring_length * repeat_count

            # Skip the characters that were repeated
            i += char_count
        else:
            # Regular character
            length += 1
            i += 1

    return length


def solve(puzzle_input: str) -> str:
    """Solve part 2.

    Approach:
        Calculate the decompressed length using version 2 of the
        format, where markers within decompressed data are recursively
        processed.

    Args:
        puzzle_input: Raw puzzle input string

    Returns:
        The decompressed length

    """
    return str(decompress_length_v2(puzzle_input))


if __name__ == "__main__":
    from aoc.helpers import read_puzzle_input

    answer = solve(read_puzzle_input(2016, 9))
    print(answer)
