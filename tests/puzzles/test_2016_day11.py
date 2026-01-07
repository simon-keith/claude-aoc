"""Tests for Advent of Code 2016 Day 11."""

from aoc.puzzles.year2016.day11 import part1


class TestPart1:
    def test_example(self):
        """Test with example configuration."""
        puzzle_input = """The first floor contains a hydrogen-compatible microchip and a lithium-compatible microchip.
The second floor contains a hydrogen generator.
The third floor contains a lithium generator.
The fourth floor contains nothing relevant."""

        assert part1.solve(puzzle_input) == "11"
