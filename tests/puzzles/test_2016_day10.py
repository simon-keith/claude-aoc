"""Tests for Advent of Code 2016 Day 10."""

from aoc.puzzles.year2016.day10 import part1, part2


class TestPart1:
    def test_example(self):
        """Test with example bot configuration."""
        puzzle_input = """value 5 goes to bot 2
bot 2 gives low to bot 1 and high to bot 0
value 3 goes to bot 1
bot 1 gives low to output 1 and high to bot 0
bot 0 gives low to output 2 and high to output 0
value 2 goes to bot 2"""

        bot_rules, initial_assignments = part1.parse_instructions(puzzle_input)
        # Bot 2 compares 2 and 5
        bot_id = part1.simulate(bot_rules, initial_assignments, 2, 5)
        assert bot_id == 2


class TestPart2:
    def test_example(self):
        """Test with example bot configuration - check outputs."""
        puzzle_input = """value 5 goes to bot 2
bot 2 gives low to bot 1 and high to bot 0
value 3 goes to bot 1
bot 1 gives low to output 1 and high to bot 0
bot 0 gives low to output 2 and high to output 0
value 2 goes to bot 2"""

        bot_rules, initial_assignments = part1.parse_instructions(puzzle_input)
        outputs = part2.simulate_and_get_outputs(bot_rules, initial_assignments)
        # Expected: output 0 has 5, output 1 has 2, output 2 has 3
        assert outputs[0] == 5
        assert outputs[1] == 2
        assert outputs[2] == 3
