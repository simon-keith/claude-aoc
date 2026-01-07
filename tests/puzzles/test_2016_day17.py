"""Tests for Advent of Code 2016 Day 17."""

from aoc.puzzles.year2016.day17 import part1, part2


class TestPart1:
    def test_example_1(self):
        """Test with passcode ihgpwlah."""
        assert part1.solve("ihgpwlah") == "DDRRRD"

    def test_example_2(self):
        """Test with passcode kglvqrro."""
        assert part1.solve("kglvqrro") == "DDUDRLRRUDRD"

    def test_example_3(self):
        """Test with passcode ulqzkmiv."""
        assert part1.solve("ulqzkmiv") == "DRURDRUDDLLDLUURRDULRLDUUDDDRR"

    def test_open_doors(self):
        """Test MD5 hash door opening."""
        assert part1.get_open_doors("hijkl", "") == "UDL"
        assert part1.get_open_doors("hijkl", "D") == "ULR"
        assert part1.get_open_doors("hijkl", "DU") == "R"
        assert part1.get_open_doors("hijkl", "DUR") == ""


class TestPart2:
    def test_example_1(self):
        """Test longest path with passcode ihgpwlah."""
        assert part2.solve("ihgpwlah") == "370"

    def test_example_2(self):
        """Test longest path with passcode kglvqrro."""
        assert part2.solve("kglvqrro") == "492"

    def test_example_3(self):
        """Test longest path with passcode ulqzkmiv."""
        assert part2.solve("ulqzkmiv") == "830"
