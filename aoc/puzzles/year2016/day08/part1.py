"""Advent of Code 2016 - Day 8 - Part 1.

Count lit pixels after executing screen instructions.
"""

import re


class Screen:
    """Represents a pixel screen with rotation operations."""

    def __init__(self, width: int, height: int) -> None:
        """Initialize screen with all pixels off.

        Args:
            width: Screen width in pixels
            height: Screen height in pixels

        """
        self.width = width
        self.height = height
        self.pixels = [[False] * width for _ in range(height)]

    def rect(self, width: int, height: int) -> None:
        """Turn on pixels in a rectangle at top-left.

        Args:
            width: Rectangle width
            height: Rectangle height

        """
        for y in range(height):
            for x in range(width):
                self.pixels[y][x] = True

    def rotate_row(self, row: int, amount: int) -> None:
        """Rotate a row right with wrapping.

        Args:
            row: Row index (0 is top)
            amount: Number of pixels to shift right

        """
        self.pixels[row] = (
            self.pixels[row][-amount:] + self.pixels[row][:-amount]
        )

    def rotate_column(self, col: int, amount: int) -> None:
        """Rotate a column down with wrapping.

        Args:
            col: Column index (0 is left)
            amount: Number of pixels to shift down

        """
        column = [self.pixels[y][col] for y in range(self.height)]
        rotated = column[-amount:] + column[:-amount]
        for y in range(self.height):
            self.pixels[y][col] = rotated[y]

    def count_lit(self) -> int:
        """Count number of lit pixels.

        Returns:
            Number of pixels that are on

        """
        return sum(sum(row) for row in self.pixels)

    def process_instruction(self, instruction: str) -> None:
        """Process a single instruction.

        Args:
            instruction: Instruction string (rect, rotate row, or rotate column)

        """
        if instruction.startswith("rect"):
            match = re.match(r"rect (\d+)x(\d+)", instruction)
            if match:
                width, height = int(match.group(1)), int(match.group(2))
                self.rect(width, height)
        elif instruction.startswith("rotate row"):
            match = re.match(r"rotate row y=(\d+) by (\d+)", instruction)
            if match:
                row, amount = int(match.group(1)), int(match.group(2))
                self.rotate_row(row, amount)
        elif instruction.startswith("rotate column"):
            match = re.match(r"rotate column x=(\d+) by (\d+)", instruction)
            if match:
                col, amount = int(match.group(1)), int(match.group(2))
                self.rotate_column(col, amount)


def solve(puzzle_input: str) -> str:
    """Solve part 1.

    Approach:
        Create a 50x6 screen, process all instructions,
        then count the number of lit pixels.

    Args:
        puzzle_input: Raw puzzle input string

    Returns:
        Number of lit pixels

    """
    screen = Screen(50, 6)
    instructions = puzzle_input.strip().split("\n")

    for instruction in instructions:
        screen.process_instruction(instruction)

    return str(screen.count_lit())


if __name__ == "__main__":
    from aoc.helpers import read_puzzle_input

    answer = solve(read_puzzle_input(2016, 8))
    print(answer)
