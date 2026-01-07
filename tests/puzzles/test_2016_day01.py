"""Tests for Advent of Code 2016 Day 1."""

from aoc.puzzles.year2016.day01 import part1, part2


class TestPart1:
    def test_example_1(self):
        """Test with R2, L3 -> 5 blocks."""
        assert part1.solve("R2, L3") == 5

    def test_example_2(self):
        """Test with R2, R2, R2 -> 2 blocks."""
        assert part1.solve("R2, R2, R2") == 2

    def test_example_3(self):
        """Test with R5, L5, R5, R3 -> 12 blocks."""
        assert part1.solve("R5, L5, R5, R3") == 12


class TestPart2:
    def test_example_1(self):
        """Test with R8, R4, R4, R8 -> 4 blocks."""
        assert part2.solve("R8, R4, R4, R8") == 4
