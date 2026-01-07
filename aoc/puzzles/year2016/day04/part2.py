"""Advent of Code 2016 - Day 4 - Part 2.

Decrypt room names using Caesar cipher to find North Pole objects.
"""

from aoc.puzzles.year2016.day04 import part1


def decrypt_name(encrypted_name: str, sector_id: int) -> str:
    """Decrypt a room name using Caesar cipher rotation.

    Args:
        encrypted_name: Encrypted name with dashes
        sector_id: Number of positions to rotate each letter

    Returns:
        Decrypted room name with spaces instead of dashes

    """
    decrypted = []

    for char in encrypted_name:
        if char == "-":
            decrypted.append(" ")
        else:
            # Rotate letter: a=0, b=1, ..., z=25
            char_pos = ord(char) - ord("a")
            rotated_pos = (char_pos + sector_id) % 26
            decrypted.append(chr(ord("a") + rotated_pos))

    return "".join(decrypted)


def solve(puzzle_input: str) -> int:
    """Solve part 2.

    Approach:
        Filter real rooms using Part 1 validation.
        Decrypt each room name using Caesar cipher.
        Find the room containing "northpole" or "north pole" in its name.
        Return its sector ID.

    Args:
        puzzle_input: Raw puzzle input string with one room per line

    Returns:
        The sector ID of the room where North Pole objects are stored

    """
    for line in puzzle_input.strip().split("\n"):
        if part1.is_real_room(line):
            encrypted_name, sector_id, _ = part1.parse_room(line)
            decrypted_name = decrypt_name(encrypted_name, sector_id)

            # Check if this is the North Pole storage room
            if "northpole" in decrypted_name.replace(" ", ""):
                return sector_id

    # No North Pole room found (shouldn't happen)
    return 0


if __name__ == "__main__":
    from aoc.helpers import read_puzzle_input

    answer = solve(read_puzzle_input(2016, 4))
    print(answer)
