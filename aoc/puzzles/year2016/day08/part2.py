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
    lines = []
    for row in screen.pixels:
        lines.append("".join("#" if pixel else "." for pixel in row))
    return "\n".join(lines)


def solve(puzzle_input: str) -> str:
    """Solve part 2.

    Approach:
        Simulate the screen operations, then render the screen
        to visually read the letters displayed. Each letter is
        5 pixels wide and 6 pixels tall.

    Args:
        puzzle_input: Raw puzzle input string

    Returns:
        The code displayed on the screen (requires manual OCR)

    """
    screen = Screen(50, 6)
    instructions = puzzle_input.strip().split("\n")

    for instruction in instructions:
        screen.process_instruction(instruction)

    # Print the screen for manual reading
    print(render_screen(screen))

    # For AoC 2016 Day 8, the answer needs to be read visually
    # Return placeholder that prompts manual reading
    return "READ_FROM_OUTPUT"


if __name__ == "__main__":
    from aoc.helpers import read_puzzle_input

    answer = solve(read_puzzle_input(2016, 8))
    print(f"\nAnswer: {answer}")
