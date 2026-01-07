"""Advent of Code 2016 - Day 8 - Part 2.

Read the code displayed on the screen.
"""

from aoc.puzzles.year2016.day08.part1 import Screen


def render_screen(screen: Screen) -> str:
    """Render the screen as a string for visual inspection.

    Args:
        screen: Screen to render

    Returns:
        String representation of the screen

    """
    return "\n".join(
        "".join("#" if pixel else "." for pixel in row) for row in screen.pixels
    )


def solve(puzzle_input: str) -> str:
    """Solve part 2.

    Approach:
        Simulate the screen operations, then render and return
        the ASCII art screen output for visual interpretation.

    Args:
        puzzle_input: Raw puzzle input string

    Returns:
        ASCII art screen output (multiline string)

    """
    screen = Screen(50, 6)
    instructions = puzzle_input.strip().split("\n")

    for instruction in instructions:
        screen.process_instruction(instruction)

    # Return the rendered screen as ASCII art
    return render_screen(screen)


if __name__ == "__main__":
    from aoc.helpers import read_puzzle_input

    answer = solve(read_puzzle_input(2016, 8))
    print(answer)
