"""Advent of Code 2016 - Day 3 - Part 1.

Count valid triangles based on triangle inequality theorem.
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
    """Solve part 1.

    Approach:
        Parse each line as three integers (triangle sides).
        Check triangle inequality: sum of any two sides > third side.
        Count valid triangles.

    Args:
        puzzle_input: Raw puzzle input string with one triangle per line

    Returns:
        The number of valid triangles

    """
    valid_count = 0

    for line in puzzle_input.strip().split("\n"):
        sides = [int(x) for x in line.split()]
        if len(sides) == 3:
            a, b, c = sides
            if is_valid_triangle(a, b, c):
                valid_count += 1

    return valid_count


if __name__ == "__main__":
    from aoc.helpers import read_puzzle_input

    answer = solve(read_puzzle_input(2016, 3))
    print(answer)
