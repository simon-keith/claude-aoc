"""Tests for Advent of Code 2016 Day 19."""

from aoc.puzzles.year2016.day19 import part1, part2


class TestPart1:
    def test_example(self):
        """Test with 5 elves."""
        assert part1.solve("5") == "3"


class TestPart2:
    def test_example(self):
        """Test with 5 elves stealing across."""
        assert part2.solve("5") == "2"
