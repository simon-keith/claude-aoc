"""Tests for Advent of Code 2016 Day 15."""

from aoc.puzzles.year2016.day15 import part1, part2


class TestPart1:
    def test_example(self):
        """Test with example disc configuration."""
        puzzle_input = """Disc #1 has 5 positions; at time=0, it is at position 4.
Disc #2 has 2 positions; at time=0, it is at position 1."""

        assert part1.solve(puzzle_input) == "5"


class TestPart2:
    def test_example_with_extra_disc(self):
        """Test with example configuration plus an extra disc."""
        puzzle_input = """Disc #1 has 5 positions; at time=0, it is at position 4.
Disc #2 has 2 positions; at time=0, it is at position 1."""

        # Part 2 adds an extra disc, so timing will be different
        result = part2.solve(puzzle_input)
        # Just verify it returns a numeric string
        assert result.isdigit()
        assert int(result) >= 5
