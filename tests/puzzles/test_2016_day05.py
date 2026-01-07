"""Tests for Advent of Code 2016 Day 5."""

from aoc.puzzles.year2016.day05 import part1, part2


class TestPart1:
    def test_example_1(self):
        """Test with door ID 'abc'."""
        assert part1.solve("abc") == "18f47a30"


class TestPart2:
    def test_example_1(self):
        """Test with door ID 'abc'."""
        assert part2.solve("abc") == "05ace8e3"
