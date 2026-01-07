"""Tests for Advent of Code 2016 Day 8."""

from aoc.puzzles.year2016.day08 import part1


class TestPart1:
    def test_example_sequence(self):
        """Test with example sequence on 7x3 screen."""
        screen = part1.Screen(7, 3)

        # rect 3x2
        screen.process_instruction("rect 3x2")
        assert screen.pixels[0][:7] == [True, True, True, False, False, False, False]
        assert screen.pixels[1][:7] == [True, True, True, False, False, False, False]
        assert screen.pixels[2][:7] == [False, False, False, False, False, False, False]

        # rotate column x=1 by 1
        screen.process_instruction("rotate column x=1 by 1")
        assert screen.pixels[0][:7] == [True, False, True, False, False, False, False]
        assert screen.pixels[1][:7] == [True, True, True, False, False, False, False]
        assert screen.pixels[2][:7] == [False, True, False, False, False, False, False]

        # rotate row y=0 by 4
        screen.process_instruction("rotate row y=0 by 4")
        assert screen.pixels[0][:7] == [False, False, False, False, True, False, True]
        assert screen.pixels[1][:7] == [True, True, True, False, False, False, False]
        assert screen.pixels[2][:7] == [False, True, False, False, False, False, False]

        # rotate column x=1 by 1
        screen.process_instruction("rotate column x=1 by 1")
        assert screen.pixels[0][:7] == [False, True, False, False, True, False, True]
        assert screen.pixels[1][:7] == [True, False, True, False, False, False, False]
        assert screen.pixels[2][:7] == [False, True, False, False, False, False, False]

        # Should have 6 pixels lit
        assert screen.count_lit() == 6
