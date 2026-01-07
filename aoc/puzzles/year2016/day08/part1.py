"""Advent of Code 2016 - Day 8 - Part 1.

Simulate a tiny LCD screen with rect and rotation operations.
"""

import re


class Screen:
    """A tiny LCD screen."""

    def __init__(self, width: int, height: int) -> None:
        """Initialize the screen with all pixels off.

        Args:
            width: Screen width in pixels
            height: Screen height in pixels

        """
        self.width = width
        self.height = height
        self.pixels = [[False] * width for _ in range(height)]

    def rect(self, width: int, height: int) -> None:
        """Turn on pixels in a rectangle at the top-left corner.

        Args:
            width: Rectangle width
            height: Rectangle height

        """
        for row in range(height):
            for col in range(width):
                self.pixels[row][col] = True

    def rotate_row(self, row: int, amount: int) -> None:
        """Rotate a row to the right by a given amount.

        Args:
            row: Row index (0 is top)
            amount: Number of pixels to shift right

        """
        # Normalize amount to avoid unnecessary full rotations
        amount = amount % self.width
        if amount == 0:
            return

        # Slice and reassemble the row with rotation
        self.pixels[row] = self.pixels[row][-amount:] + self.pixels[row][:-amount]

    def rotate_column(self, col: int, amount: int) -> None:
        """Rotate a column down by a given amount.

        Args:
            col: Column index (0 is left)
            amount: Number of pixels to shift down

        """
        # Normalize amount to avoid unnecessary full rotations
        amount = amount % self.height
        if amount == 0:
            return

        # Extract column, rotate, and write back
        column = [self.pixels[row][col] for row in range(self.height)]
        rotated = column[-amount:] + column[:-amount]
        for row in range(self.height):
            self.pixels[row][col] = rotated[row]

    def count_lit(self) -> int:
        """Count the number of lit pixels.

        Returns:
            Number of lit pixels

        """
        return sum(sum(row) for row in self.pixels)

    def process_instruction(self, instruction: str) -> None:
        """Process a single instruction.

        Args:
            instruction: Instruction string

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
        Simulate a 50x6 pixel screen, processing each instruction
        in sequence. Count the lit pixels at the end.

    Args:
        puzzle_input: Raw puzzle input string

    Returns:
        The number of lit pixels

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
