"""Tests for Advent of Code 2016 Day 2."""

from aoc.puzzles.year2016.day02 import part1, part2


class TestPart1:
    def test_example(self):
        """Test with the example input from the puzzle description."""
        puzzle_input = """ULL
RRDDD
LURDL
UUUUD"""
        assert part1.solve(puzzle_input) == "1985"


class TestPart2:
    def test_example(self):
        """Test with the diamond keypad layout."""
        puzzle_input = """ULL
RRDDD
LURDL
UUUUD"""
        assert part2.solve(puzzle_input) == "5DB3"
