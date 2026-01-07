"""Advent of Code 2016 - Day 17 - Part 1.

Find shortest path through MD5-based door maze.
"""

import hashlib
from collections import deque


def get_open_doors(passcode: str, path: str) -> str:
    """Get which doors are open based on MD5 hash.

    Args:
        passcode: The vault passcode
        path: Path taken so far (e.g., "UDLR")

    Returns:
        String of open door directions (subset of "UDLR")

    """
    hash_input = passcode + path
    md5_hash = hashlib.md5(hash_input.encode(), usedforsecurity=False).hexdigest()
    open_chars = 'bcdef'

    open_doors = ''
    directions = 'UDLR'
    for i, direction in enumerate(directions):
        if md5_hash[i] in open_chars:
            open_doors += direction

    return open_doors


def find_shortest_path(passcode: str) -> str:
    """Find shortest path to vault using BFS.

    Args:
        passcode: The vault passcode

    Returns:
        Shortest path string (e.g., "DDRRRD")

    """
    # Start at (0, 0), goal is (3, 3)
    # BFS queue: (x, y, path)
    queue = deque([(0, 0, '')])

    while queue:
        x, y, path = queue.popleft()

        # Check if we reached the vault
        if x == 3 and y == 3:
            return path

        # Get open doors
        open_doors = get_open_doors(passcode, path)

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

    return ''  # No path found


def solve(puzzle_input: str) -> str:
    """Solve part 1.

    Approach:
        Use BFS to find shortest path through vault
        MD5 hash determines which doors are open at each state

    Args:
        puzzle_input: Raw puzzle input string

    Returns:
        The answer to part 1

    """
    passcode = puzzle_input.strip()
    return find_shortest_path(passcode)


if __name__ == "__main__":
    from aoc.helpers import read_puzzle_input

    answer = solve(read_puzzle_input(2016, 17))
    print(answer)
