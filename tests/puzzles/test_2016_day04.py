"""Tests for Advent of Code 2016 Day 4."""

from aoc.puzzles.year2016.day04 import part1, part2


class TestPart1:
    def test_example_1(self):
        """Test with real room: aaaaa-bbb-z-y-x-123[abxyz]."""
        assert part1.is_real_room("aaaaa-bbb-z-y-x-123[abxyz]") is True

    def test_example_2(self):
        """Test with real room: a-b-c-d-e-f-g-h-987[abcde]."""
        assert part1.is_real_room("a-b-c-d-e-f-g-h-987[abcde]") is True

    def test_example_3(self):
        """Test with real room: not-a-real-room-404[oarel]."""
        assert part1.is_real_room("not-a-real-room-404[oarel]") is True

    def test_example_4(self):
        """Test with decoy room: totally-real-room-200[decoy]."""
        assert part1.is_real_room("totally-real-room-200[decoy]") is False

    def test_example_sum(self):
        """Test sum of sector IDs."""
        puzzle_input = """aaaaa-bbb-z-y-x-123[abxyz]
a-b-c-d-e-f-g-h-987[abcde]
not-a-real-room-404[oarel]
totally-real-room-200[decoy]"""
        assert part1.solve(puzzle_input) == 1514


class TestPart2:
    def test_decrypt_example(self):
        """Test decryption: qzmt-zixmtkozy-ivhz-343 -> very encrypted name."""
        decrypted = part2.decrypt_name("qzmt-zixmtkozy-ivhz", 343)
        assert decrypted == "very encrypted name"
