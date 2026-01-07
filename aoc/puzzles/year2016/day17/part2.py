"""Advent of Code 2016 - Day 17 - Part 2.

Find longest path through MD5-based door maze.
"""

from collections import deque

from aoc.puzzles.year2016.day17 import part1


def find_longest_path_length(passcode: str) -> int:
    """Find longest path to vault using BFS.

    Args:
        passcode: The vault passcode

    Returns:
        Length of longest path

    """
    # Start at (0, 0), goal is (3, 3)
    # BFS queue: (x, y, path)
    queue = deque([(0, 0, '')])
    longest_path_length = 0

    while queue:
        x, y, path = queue.popleft()

        # Check if we reached the vault
        if x == 3 and y == 3:
            longest_path_length = max(longest_path_length, len(path))
            continue  # Don't explore further from vault

        # Get open doors
        open_doors = part1.get_open_doors(passcode, path)

        # Try each direction
        moves = {
            'U': (0, -1),
            'D': (0, 1),
            'L': (-1, 0),
            'R': (1, 0)
        }

        for direction in open_doors:
            dx, dy = moves[direction]
            nx, ny = x + dx, y + dy

            # Check bounds (4x4 grid)
            if 0 <= nx < 4 and 0 <= ny < 4:
                queue.append((nx, ny, path + direction))

    return longest_path_length


def solve(puzzle_input: str) -> str:
    """Solve part 2.

    Approach:
        Use BFS to explore all paths
        Find the longest path that reaches the vault

    Args:
        puzzle_input: Raw puzzle input string

    Returns:
        The answer to part 2

    """
    passcode = puzzle_input.strip()
    return str(find_longest_path_length(passcode))


if __name__ == "__main__":
    from aoc.helpers import read_puzzle_input

    answer = solve(read_puzzle_input(2016, 17))
    print(answer)
