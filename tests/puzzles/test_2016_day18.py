"""Tests for Advent of Code 2016 Day 18."""

from aoc.puzzles.year2016.day18 import part1, part2


class TestPart1:
    def test_example_small(self):
        """Test with small 3-row example."""
        first_row = "..^^."
        # Row 1: ..^^.
        # Row 2: .^^^^
        # Row 3: ^^..^
        # Safe tiles: 2 + 1 + 2 = 6 (out of 15 total)
        assert part1.count_safe_tiles(first_row, 3) == 6

    def test_example_large(self):
        """Test with 10-row example."""
        first_row = ".^^.^.^^^^"
        assert part1.solve(first_row, total_rows=10) == "38"

    def test_row_generation(self):
        """Test row generation."""
        assert part1.generate_next_row("..^^.") == ".^^^^"
        assert part1.generate_next_row(".^^^^") == "^^..^"


class TestPart2:
    def test_reuses_part1(self):
        """Test that part2 reuses part1 with more rows."""
        # Part 2 uses total_rows=400000, just verify it runs
        assert part2.solve("..^^.") != ""
