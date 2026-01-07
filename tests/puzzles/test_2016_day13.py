"""Tests for Advent of Code 2016 Day 13."""

from aoc.puzzles.year2016.day13 import part1, part2


class TestPart1:
    def test_example(self):
        """Test with favorite number 10, target (7,4)."""
        assert part1.find_shortest_path(10, 7, 4) == 11


class TestPart2:
    def test_count_reachable(self):
        """Test counting locations reachable in 50 steps."""
        # With favorite number 10, count locations within 50 steps
        result = part2.count_reachable(10, 50)
        # Should be a reasonable number
        assert result > 0
        assert result < 10000
