"""Tests for Advent of Code 2016 Day 1."""
import importlib.util
from pathlib import Path


def load_module(filepath):
    """Dynamically load a Python module from a file path."""
    spec = importlib.util.spec_from_file_location("part1", filepath)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


part1 = load_module(Path(__file__).parent.parent.parent / "puzzles/2016/day01/part1.py")
part2 = load_module(Path(__file__).parent.parent.parent / "puzzles/2016/day01/part2.py")


class TestPart1:
    def test_example_1(self):
        """Test with R2, L3 -> 5 blocks."""
        original = part1.read_input
        part1.read_input = lambda: "R2, L3"

        result = part1.solve()
        assert result == 5

        part1.read_input = original

    def test_example_2(self):
        """Test with R2, R2, R2 -> 2 blocks."""
        original = part1.read_input
        part1.read_input = lambda: "R2, R2, R2"

        result = part1.solve()
        assert result == 2

        part1.read_input = original

    def test_example_3(self):
        """Test with R5, L5, R5, R3 -> 12 blocks."""
        original = part1.read_input
        part1.read_input = lambda: "R5, L5, R5, R3"

        result = part1.solve()
        assert result == 12

        part1.read_input = original


class TestPart2:
    def test_example_1(self):
        """Test with R8, R4, R4, R8 -> 4 blocks."""
        original = part2.read_input
        part2.read_input = lambda: "R8, R4, R4, R8"

        result = part2.solve()
        assert result == 4

        part2.read_input = original
