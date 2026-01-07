"""Tests for Advent of Code 2016 Day 6."""

from aoc.puzzles.year2016.day06 import part1, part2


class TestPart1:
    def test_example_1(self):
        """Test with example messages."""
        puzzle_input = """eedadn
drvtee
eandsr
raavrd
atevrs
tsrnev
sdttsa
rasrtv
nssdts
ntnada
svetve
tesnvt
vntsnd
vrdear
dvrsen
enarar"""
        assert part1.solve(puzzle_input) == "easter"


class TestPart2:
    def test_example_1(self):
        """Test with example messages."""
        puzzle_input = """eedadn
drvtee
eandsr
raavrd
atevrs
tsrnev
sdttsa
rasrtv
nssdts
ntnada
svetve
tesnvt
vntsnd
vrdear
dvrsen
enarar"""
        assert part2.solve(puzzle_input) == "advent"
