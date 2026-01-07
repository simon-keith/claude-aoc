"""Advent of Code 2016 - Day 18 - Part 1.

Count safe tiles in trap-filled room using cellular automaton rules.
"""


def is_trap(left: str, center: str, right: str) -> bool:
    """Determine if a tile is a trap based on the three tiles above it.

    Args:
        left: Tile to the left (or '.' if at edge)
        center: Tile directly above
        right: Tile to the right (or '.' if at edge)

    Returns:
        True if the new tile is a trap, False if safe

    """
    # Trap conditions
    if left == '^' and center == '^' and right == '.':
        return True
    if left == '.' and center == '^' and right == '^':
        return True
    if left == '^' and center == '.' and right == '.':
        return True
    return left == '.' and center == '.' and right == '^'


def generate_next_row(previous_row: str) -> str:
    """Generate the next row based on trap rules.

    Args:
        previous_row: The previous row of tiles

    Returns:
        The next row of tiles

    """
    next_row = []
    for i in range(len(previous_row)):
        left = previous_row[i - 1] if i > 0 else '.'
        center = previous_row[i]
        right = previous_row[i + 1] if i < len(previous_row) - 1 else '.'

        if is_trap(left, center, right):
            next_row.append('^')
        else:
            next_row.append('.')

    return ''.join(next_row)


def count_safe_tiles(first_row: str, total_rows: int) -> int:
    """Count safe tiles in the room.

    Args:
        first_row: The first row of tiles
        total_rows: Total number of rows to generate

    Returns:
        Number of safe tiles

    """
    safe_count = first_row.count('.')
    current_row = first_row

    for _ in range(total_rows - 1):
        current_row = generate_next_row(current_row)
        safe_count += current_row.count('.')

    return safe_count


def solve(puzzle_input: str, total_rows: int = 40) -> str:
    """Solve part 1.

    Approach:
        Generate rows using cellular automaton rules
        Count safe tiles (.) across all rows

    Args:
        puzzle_input: Raw puzzle input string
        total_rows: Total number of rows (default 40)

    Returns:
        The answer to part 1

    """
    first_row = puzzle_input.strip()
    return str(count_safe_tiles(first_row, total_rows))


if __name__ == "__main__":
    from aoc.helpers import read_puzzle_input

    answer = solve(read_puzzle_input(2016, 18))
    print(answer)
