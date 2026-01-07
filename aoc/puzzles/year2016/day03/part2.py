"""Advent of Code 2016 - Day 3 - Part 2.

Count valid triangles reading by columns instead of rows.
"""


def is_valid_triangle(a: int, b: int, c: int) -> bool:
    """Check if three sides form a valid triangle.

    A valid triangle must satisfy the triangle inequality:
    the sum of any two sides must be greater than the third side.

    Args:
        a: First side length
        b: Second side length
        c: Third side length

    Returns:
        True if the three sides form a valid triangle

    """
    return a + b > c and a + c > b and b + c > a


def solve(puzzle_input: str) -> int:
    """Solve part 2.

    Approach:
        Read input by columns instead of rows.
        Every 3 rows form 3 triangles (one per column).
        Check triangle inequality for each vertical triangle.
        Count valid triangles.

    Args:
        puzzle_input: Raw puzzle input string with triangle data in columns

    Returns:
        The number of valid triangles when reading by columns

    """
    lines = puzzle_input.strip().split("\n")
    valid_count = 0

    # Process 3 rows at a time
    for i in range(0, len(lines), 3):
        if i + 2 < len(lines):
            # Parse the three rows
            row1 = [int(x) for x in lines[i].split()]
            row2 = [int(x) for x in lines[i + 1].split()]
            row3 = [int(x) for x in lines[i + 2].split()]

            # Check each of the three vertical triangles
            for col in range(3):
                if is_valid_triangle(row1[col], row2[col], row3[col]):
                    valid_count += 1

    return valid_count


if __name__ == "__main__":
    from aoc.helpers import read_puzzle_input

    answer = solve(read_puzzle_input(2016, 3))
    print(answer)
