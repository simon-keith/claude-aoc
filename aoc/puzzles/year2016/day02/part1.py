"""Advent of Code 2016 - Day 2 - Part 1.

Find the bathroom code by following keypad navigation instructions.
"""


def solve(puzzle_input: str) -> str:
    """Solve part 1.

    Approach:
        Simulate navigating a 3x3 keypad starting at position "5".
        For each line of instructions, move U/D/L/R and track position.
        Ignore moves that would go off the keypad.
        Record the digit at the end of each line.

    Args:
        puzzle_input: Raw puzzle input string with one instruction line per button

    Returns:
        The bathroom code as a string of digits

    """
    # Define the 3x3 keypad layout as a 2D grid
    # Using (row, col) coordinates where (0, 0) is top-left
    keypad = [
        ["1", "2", "3"],
        ["4", "5", "6"],
        ["7", "8", "9"],
    ]

    # Start at "5" which is position (1, 1)
    row, col = 1, 1
    code = []

    # Process each line of instructions
    for line in puzzle_input.strip().split("\n"):
        for direction in line:
            # Calculate new position based on direction
            new_row, new_col = row, col

            if direction == "U":
                new_row = row - 1
            elif direction == "D":
                new_row = row + 1
            elif direction == "L":
                new_col = col - 1
            elif direction == "R":
                new_col = col + 1

            # Only move if the new position is valid (within bounds)
            if 0 <= new_row < 3 and 0 <= new_col < 3:
                row, col = new_row, new_col

        # Record the button we're on at the end of this line
        code.append(keypad[row][col])

    return "".join(code)


if __name__ == "__main__":
    from aoc.helpers import read_puzzle_input

    answer = solve(read_puzzle_input(2016, 2))
    print(answer)
