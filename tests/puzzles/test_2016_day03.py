"""Tests for Advent of Code 2016 Day 3."""

from aoc.puzzles.year2016.day03 import part1, part2


class TestPart1:
    def test_example_1(self):
        """Test with invalid triangle 5 10 25."""
        assert part1.solve("5 10 25") == 0

    def test_example_2(self):
        """Test with valid triangle 3 4 5."""
        assert part1.solve("3 4 5") == 1

    def test_example_3(self):
        """Test with multiple triangles."""
        assert part1.solve("5 10 25\n3 4 5\n10 10 10") == 2


class TestPart2:
    def test_example_1(self):
        """Test with example from puzzle description."""
        puzzle_input = """101 301 501
102 302 502
103 303 503
201 401 601
202 402 602
203 403 603"""
        # Triangles formed by columns:
        # Column 1: (101, 102, 103), (201, 202, 203)
        # Column 2: (301, 302, 303), (401, 402, 403)
        # Column 3: (501, 502, 503), (601, 602, 603)
        # All 6 should be valid triangles
        assert part2.solve(puzzle_input) == 6
