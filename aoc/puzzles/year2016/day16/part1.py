"""Advent of Code 2016 - Day 16 - Part 1.

Generate data using modified dragon curve and compute checksum.
"""


def dragon_curve(data: str) -> str:
    """Apply one iteration of the modified dragon curve.

    Args:
        data: Current data string

    Returns:
        Data after one dragon curve iteration

    """
    a = data
    b = a[::-1]  # Reverse
    b = b.translate(str.maketrans('01', '10'))  # Flip bits
    return a + '0' + b


def generate_data(initial: str, length: int) -> str:
    """Generate data until it reaches at least the target length.

    Args:
        initial: Initial state
        length: Target length

    Returns:
        Generated data trimmed to target length

    """
    data = initial
    while len(data) < length:
        data = dragon_curve(data)
    return data[:length]


def compute_checksum(data: str) -> str:
    """Compute checksum by pairing characters until odd length.

    Args:
        data: Data to checksum

    Returns:
        Checksum with odd length

    """
    checksum = data
    while len(checksum) % 2 == 0:
        new_checksum = []
        for i in range(0, len(checksum), 2):
            pair = checksum[i:i+2]
            if pair[0] == pair[1]:
                new_checksum.append('1')
            else:
                new_checksum.append('0')
        checksum = ''.join(new_checksum)
    return checksum


def solve(puzzle_input: str, disk_length: int = 272) -> str:
    """Solve part 1.

    Approach:
        Generate data using dragon curve until target length
        Compute checksum by pairing until odd length

    Args:
        puzzle_input: Raw puzzle input string
        disk_length: Target disk length (default 272 for part 1)

    Returns:
        The answer to part 1

    """
    initial_state = puzzle_input.strip()

    data = generate_data(initial_state, disk_length)
    return compute_checksum(data)


if __name__ == "__main__":
    from aoc.helpers import read_puzzle_input

    answer = solve(read_puzzle_input(2016, 16))
    print(answer)
