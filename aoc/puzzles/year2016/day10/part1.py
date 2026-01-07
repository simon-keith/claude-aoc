"""Advent of Code 2016 - Day 10 - Part 1.

Simulate bot factory and find bot comparing specific chips.
"""

import re
from collections import defaultdict
from typing import TypedDict


class BotRule(TypedDict):
    """Bot rule specifying where to send low and high chips."""

    low_type: str  # "bot" or "output"
    low_id: int
    high_type: str  # "bot" or "output"
    high_id: int


def parse_instructions(puzzle_input: str) -> tuple[dict[int, BotRule], list[tuple[int, int]]]:
    """Parse bot instructions and initial chip assignments.

    Args:
        puzzle_input: Raw puzzle input string

    Returns:
        Tuple of (bot_rules, initial_assignments)
        - bot_rules: Dict mapping bot_id to its rule
        - initial_assignments: List of (chip_value, bot_id) tuples

    """
    bot_rules: dict[int, BotRule] = {}
    initial_assignments: list[tuple[int, int]] = []

    for line in puzzle_input.strip().split("\n"):
        if line.startswith("value"):
            match = re.match(r"value (\d+) goes to bot (\d+)", line)
            if match:
                value, bot_id = int(match.group(1)), int(match.group(2))
                initial_assignments.append((value, bot_id))
        elif line.startswith("bot"):
            match = re.match(
                r"bot (\d+) gives low to (bot|output) (\d+) and high to (bot|output) (\d+)",
                line,
            )
            if match:
                bot_id = int(match.group(1))
                low_type, low_id = match.group(2), int(match.group(3))
                high_type, high_id = match.group(4), int(match.group(5))
                bot_rules[bot_id] = BotRule(
                    low_type=low_type, low_id=low_id, high_type=high_type, high_id=high_id
                )

    return bot_rules, initial_assignments


def simulate(
    bot_rules: dict[int, BotRule],
    initial_assignments: list[tuple[int, int]],
    target_low: int,
    target_high: int,
) -> int:
    """Simulate bot factory and find bot comparing target chips.

    Args:
        bot_rules: Dict mapping bot_id to its rule
        initial_assignments: List of (chip_value, bot_id) tuples
        target_low: Lower target chip value
        target_high: Higher target chip value

    Returns:
        Bot ID that compares the target chips

    """
    # Track chips held by each bot
    bot_chips: dict[int, list[int]] = defaultdict(list)
    outputs: dict[int, int] = {}

    # Initial chip assignments
    for chip_value, bot_id in initial_assignments:
        bot_chips[bot_id].append(chip_value)

    # Process until we find the target bot
    while True:
        # Find a bot with 2 chips
        active_bot = None
        for bot_id, chips in bot_chips.items():
            if len(chips) == 2:
                active_bot = bot_id
                break

        if active_bot is None:
            # No more bots with 2 chips
            break

        # Get the chips and sort them
        chips = sorted(bot_chips[active_bot])
        low_chip, high_chip = chips[0], chips[1]

        # Check if this is the target bot
        if low_chip == target_low and high_chip == target_high:
            return active_bot

        # Clear this bot's chips
        bot_chips[active_bot] = []

        # Execute the bot's rule
        rule = bot_rules[active_bot]

        # Send low chip
        if rule["low_type"] == "bot":
            bot_chips[rule["low_id"]].append(low_chip)
        else:
            outputs[rule["low_id"]] = low_chip

        # Send high chip
        if rule["high_type"] == "bot":
            bot_chips[rule["high_id"]].append(high_chip)
        else:
            outputs[rule["high_id"]] = high_chip

    return -1  # Target not found


def solve(puzzle_input: str) -> str:
    """Solve part 1.

    Approach:
        Parse instructions, then simulate the bot factory until
        we find the bot that compares chips 61 and 17.

    Args:
        puzzle_input: Raw puzzle input string

    Returns:
        The bot ID that compares chips 61 and 17

    """
    bot_rules, initial_assignments = parse_instructions(puzzle_input)
    bot_id = simulate(bot_rules, initial_assignments, 17, 61)
    return str(bot_id)


if __name__ == "__main__":
    from aoc.helpers import read_puzzle_input

    answer = solve(read_puzzle_input(2016, 10))
    print(answer)
