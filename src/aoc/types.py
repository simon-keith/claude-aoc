"""Type definitions for the AoC solver."""

from dataclasses import dataclass


@dataclass
class SolveResult:
    """Result from solving a puzzle.

    Attributes:
        year: The year of the puzzle
        day: The day of the puzzle
        part1_answer: The answer to part 1 (None if not solved)
        part1_time: Execution time for part 1 in seconds
        part2_answer: The answer to part 2 (None if not solved)
        part2_time: Execution time for part 2 in seconds

    """

    year: int
    day: int
    part1_answer: int | str | None
    part1_time: float
    part2_answer: int | str | None
    part2_time: float
