"""Tests for Advent of Code 2016 Day 14."""

from aoc.puzzles.year2016.day14 import part1


class TestPart1:
    def test_example(self):
        """Test with salt 'abc'."""
        assert part1.find_64th_key("abc") == 22728
