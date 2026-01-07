"""Tests for Advent of Code 2016 Day 16."""

from aoc.puzzles.year2016.day16 import part1, part2


class TestPart1:
    def test_dragon_curve_examples(self):
        """Test dragon curve transformation examples."""
        assert part1.dragon_curve("1") == "100"
        assert part1.dragon_curve("0") == "001"
        assert part1.dragon_curve("11111") == "11111000000"
        assert part1.dragon_curve("111100001010") == "1111000010100101011110000"

    def test_checksum_example(self):
        """Test checksum computation."""
        assert part1.compute_checksum("110010110100") == "100"

    def test_full_example(self):
        """Test full example with length 20."""
        assert part1.solve("10000\n", disk_length=20) == "01100"


class TestPart2:
    def test_reuses_part1(self):
        """Test that part2 reuses part1 with larger disk."""
        # Part 2 uses disk_length=35651584, just verify it runs
        assert part2.solve("10000") != ""
