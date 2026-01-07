"""Tests for Advent of Code 2016 Day 20."""

from aoc.puzzles.year2016.day20 import part1, part2


class TestPart1:
    def test_example(self):
        """Test with example blacklist."""
        puzzle_input = """5-8
0-2
4-7"""
        assert part1.solve(puzzle_input) == "3"


class TestPart2:
    def test_example(self):
        """Test counting allowed IPs."""
        puzzle_input = """5-8
0-2
4-7"""
        # With max_ip=9: blocked are 0-2,4-8, allowed are 3,9 = 2
        assert part2.count_allowed_ips(part1.parse_ranges(puzzle_input), max_ip=9) == 2
