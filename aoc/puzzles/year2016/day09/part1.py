"""Advent of Code 2016 - Day 9 - Part 1.

Calculate decompressed length of compressed file.
"""



def decompress_length(compressed: str) -> int:
    """Calculate the decompressed length without actually decompressing.

    Approach:
        Parse the compressed string character by character.
        When encountering a marker (NxM), skip the next N characters
        but count them M times in the total length. Markers within
        decompressed data are treated as literal characters.

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

            # Add the decompressed length (without actually decompressing)
            length += char_count * repeat_count

            # Skip the characters that would be repeated
            i += char_count
        else:
            # Regular character
            length += 1
            i += 1

    return length


def solve(puzzle_input: str) -> str:
    """Solve part 1.

    Approach:
        Calculate the decompressed length by parsing markers
        and counting repeated characters without full decompression.

    Args:
        puzzle_input: Raw puzzle input string

    Returns:
        The decompressed length

    """
    return str(decompress_length(puzzle_input))


if __name__ == "__main__":
    from aoc.helpers import read_puzzle_input

    answer = solve(read_puzzle_input(2016, 9))
    print(answer)
