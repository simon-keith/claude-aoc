"""Advent of Code 2016 - Day 2 - Part 2.

Find the bathroom code using a diamond-shaped keypad layout.
"""


def solve(puzzle_input: str) -> str:
    """Solve part 2.

    Approach:
        Similar to Part 1, but with a diamond-shaped keypad layout.
        The keypad is irregular, so we use a dictionary to map valid
        positions to their button values and track valid movements.

    Args:
        puzzle_input: Raw puzzle input string with one instruction line per button

    Returns:
        The bathroom code as a string (may contain hex digits A-D)

    """
    # Define the diamond-shaped keypad as a dictionary
    # Using (row, col) coordinates where (0, 2) is top (button "1")
    keypad = {
        (0, 2): "1",
        (1, 1): "2",
        (1, 2): "3",
        (1, 3): "4",
        (2, 0): "5",
        (2, 1): "6",
        (2, 2): "7",
        (2, 3): "8",
        (2, 4): "9",
        (3, 1): "A",
        (3, 2): "B",
        (3, 3): "C",
        (4, 2): "D",
    }

    # Start at "5" which is position (2, 0)
    row, col = 2, 0
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

            # Only move if the new position exists in the keypad
            if (new_row, new_col) in keypad:
                row, col = new_row, new_col

        # Record the button we're on at the end of this line
        code.append(keypad[(row, col)])

    return "".join(code)


if __name__ == "__main__":
    from aoc.helpers import read_puzzle_input

    answer = solve(read_puzzle_input(2016, 2))
    print(answer)
