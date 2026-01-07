"""Advent of Code 2016 - Day 13 - Part 2.

Count locations reachable in at most 50 steps.
"""

from collections import deque

from aoc.puzzles.year2016.day13.part1 import is_open_space


def count_reachable(favorite: int, max_steps: int) -> int:
    """Count locations reachable in at most max_steps.

    Args:
        favorite: Office designer's favorite number
        max_steps: Maximum number of steps

    Returns:
        Number of distinct reachable locations

    """
    queue = deque([(1, 1, 0)])  # (x, y, steps)
    visited = {(1, 1)}

    while queue:
        x, y, steps = queue.popleft()

        if steps >= max_steps:
            continue

        # Try all 4 directions
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy

            if (nx, ny) not in visited and is_open_space(nx, ny, favorite):
                visited.add((nx, ny))
                queue.append((nx, ny, steps + 1))

    return len(visited)


def solve(puzzle_input: str) -> str:
    """Solve part 2.

    Approach:
        Use BFS to explore all reachable locations within 50 steps.

    Args:
        puzzle_input: Raw puzzle input string (favorite number)

    Returns:
        Number of reachable locations

    """
    favorite = int(puzzle_input.strip())
    return str(count_reachable(favorite, 50))


if __name__ == "__main__":
    from aoc.helpers import read_puzzle_input

    answer = solve(read_puzzle_input(2016, 13))
    print(answer)
