"""Tests for Advent of Code 2016 Day 7."""

from aoc.puzzles.year2016.day07 import part1, part2


class TestPart1:
    def test_example_1(self):
        """Test with abba[mnop]qrst - supports TLS."""
        assert part1.supports_tls("abba[mnop]qrst") is True

    def test_example_2(self):
        """Test with abcd[bddb]xyyx - does not support TLS."""
        assert part1.supports_tls("abcd[bddb]xyyx") is False

    def test_example_3(self):
        """Test with aaaa[qwer]tyui - does not support TLS."""
        assert part1.supports_tls("aaaa[qwer]tyui") is False

    def test_example_4(self):
        """Test with ioxxoj[asdfgh]zxcvbn - supports TLS."""
        assert part1.supports_tls("ioxxoj[asdfgh]zxcvbn") is True


class TestPart2:
    def test_example_1(self):
        """Test with aba[bab]xyz - supports SSL."""
        assert part2.supports_ssl("aba[bab]xyz") is True

    def test_example_2(self):
        """Test with xyx[xyx]xyx - does not support SSL."""
        assert part2.supports_ssl("xyx[xyx]xyx") is False

    def test_example_3(self):
        """Test with aaa[kek]eke - supports SSL."""
        assert part2.supports_ssl("aaa[kek]eke") is True

    def test_example_4(self):
        """Test with zazbz[bzb]cdb - supports SSL."""
        assert part2.supports_ssl("zazbz[bzb]cdb") is True
