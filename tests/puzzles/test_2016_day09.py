"""Tests for Advent of Code 2016 Day 9."""

from aoc.puzzles.year2016.day09 import part1, part2


class TestPart1:
    def test_example_1(self):
        """Test with ADVENT - no markers."""
        assert part1.decompress_length("ADVENT") == 6

    def test_example_2(self):
        """Test with A(1x5)BC - repeat B 5 times."""
        assert part1.decompress_length("A(1x5)BC") == 7

    def test_example_3(self):
        """Test with (3x3)XYZ - repeat XYZ 3 times."""
        assert part1.decompress_length("(3x3)XYZ") == 9

    def test_example_4(self):
        """Test with A(2x2)BCD(2x2)EFG - double BC and EF."""
        assert part1.decompress_length("A(2x2)BCD(2x2)EFG") == 11

    def test_example_5(self):
        """Test with (6x1)(1x3)A - marker within data."""
        assert part1.decompress_length("(6x1)(1x3)A") == 6

    def test_example_6(self):
        """Test with X(8x2)(3x3)ABCY - nested marker not processed."""
        assert part1.decompress_length("X(8x2)(3x3)ABCY") == 18


class TestPart2:
    def test_example_1(self):
        """Test with (3x3)XYZ - no nested markers."""
        assert part2.decompress_length_v2("(3x3)XYZ") == 9

    def test_example_2(self):
        """Test with X(8x2)(3x3)ABCY - recursive processing."""
        assert part2.decompress_length_v2("X(8x2)(3x3)ABCY") == 20

    def test_example_3(self):
        """Test with deeply nested markers."""
        assert part2.decompress_length_v2("(27x12)(20x12)(13x14)(7x10)(1x12)A") == 241920

    def test_example_4(self):
        """Test with complex nested markers."""
        assert (
            part2.decompress_length_v2("(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN")
            == 445
        )
