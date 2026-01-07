"""Tests for Advent of Code 2016 Day 12."""

from aoc.puzzles.year2016.day12 import part1, part2


class TestPart1:
    def test_example(self):
        """Test with example program."""
        puzzle_input = """cpy 41 a
inc a
inc a
dec a
jnz a 2
dec a"""

        assert part1.solve(puzzle_input) == "42"


class TestPart2:
    def test_example(self):
        """Test with example program and c=1."""
        puzzle_input = """cpy 41 a
inc a
inc a
dec a
jnz a 2
dec a"""

        assert part2.solve(puzzle_input) == "42"
