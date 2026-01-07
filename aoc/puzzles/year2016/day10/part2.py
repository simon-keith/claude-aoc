"""Advent of Code 2016 - Day 10 - Part 2.

Find product of chips in outputs 0, 1, and 2.
"""

from collections import defaultdict

from aoc.puzzles.year2016.day10.part1 import BotRule, parse_instructions


def simulate_and_get_outputs(
    bot_rules: dict[int, BotRule], initial_assignments: list[tuple[int, int]]
) -> dict[int, int]:
    """Simulate bot factory and return all output values.

    Args:
        bot_rules: Dict mapping bot_id to its rule
        initial_assignments: List of (chip_value, bot_id) tuples

    Returns:
        Dict mapping output_id to chip value

    """
    # Track chips held by each bot
    bot_chips: dict[int, list[int]] = defaultdict(list)
    outputs: dict[int, int] = {}

    # Initial chip assignments
    for chip_value, bot_id in initial_assignments:
        bot_chips[bot_id].append(chip_value)

    # Process all bots
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

    return outputs


def solve(puzzle_input: str) -> str:
    """Solve part 2.

    Approach:
        Simulate the bot factory and collect all output values.
        Return the product of chips in outputs 0, 1, and 2.

    Args:
        puzzle_input: Raw puzzle input string

    Returns:
        Product of chips in outputs 0, 1, and 2

    """
    bot_rules, initial_assignments = parse_instructions(puzzle_input)
    outputs = simulate_and_get_outputs(bot_rules, initial_assignments)

    product = outputs[0] * outputs[1] * outputs[2]
    return str(product)


if __name__ == "__main__":
    from aoc.helpers import read_puzzle_input

    answer = solve(read_puzzle_input(2016, 10))
    print(answer)
