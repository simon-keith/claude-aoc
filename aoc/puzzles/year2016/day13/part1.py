"""Advent of Code 2016 - Day 13 - Part 1.

Find shortest path in procedurally generated maze.
"""

from collections import deque


def is_open_space(x: int, y: int, favorite: int) -> bool:
    """Check if a coordinate is an open space.

    Args:
        x: X coordinate
        y: Y coordinate
        favorite: Office designer's favorite number

    Returns:
        True if open space, False if wall

    """
    if x < 0 or y < 0:
        return False

    value = x * x + 3 * x + 2 * x * y + y + y * y + favorite
    # Count 1 bits
    return value.bit_count() % 2 == 0


def find_shortest_path(favorite: int, target_x: int, target_y: int) -> int:
    """Find shortest path from (1,1) to target using BFS.

    Args:
        favorite: Office designer's favorite number
        target_x: Target X coordinate
        target_y: Target Y coordinate

    Returns:
        Minimum number of steps

    """
    queue = deque([(1, 1, 0)])  # (x, y, steps)
    visited = {(1, 1)}

    while queue:
        x, y, steps = queue.popleft()

        if x == target_x and y == target_y:
            return steps

        # Try all 4 directions
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy

            if (nx, ny) not in visited and is_open_space(nx, ny, favorite):
                visited.add((nx, ny))
                queue.append((nx, ny, steps + 1))

    return -1  # No path found


def solve(puzzle_input: str) -> str:
    """Solve part 1.

    Approach:
        Use BFS to find shortest path from (1,1) to (31,39)
        in a procedurally generated maze.

    Args:
        puzzle_input: Raw puzzle input string (favorite number)

    Returns:
        Minimum number of steps

    """
    favorite = int(puzzle_input.strip())
    return str(find_shortest_path(favorite, 31, 39))


if __name__ == "__main__":
    from aoc.helpers import read_puzzle_input

    answer = solve(read_puzzle_input(2016, 13))
    print(answer)
