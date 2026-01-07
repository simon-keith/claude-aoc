"""Display and run functions for AoC solver results."""

import importlib
from pathlib import Path

from aoc.helpers import read_puzzle_input, timer
from aoc.types import SolveResult


def run_day(year: int, day: int) -> SolveResult:
    """Run both parts of a puzzle and collect results.

    Args:
        year: Year of the puzzle
        day: Day of the puzzle (1-25)

    Returns:
        SolveResult with answers and execution times

    """
    # Import part1 and part2 modules dynamically
    part1 = importlib.import_module(f"aoc.puzzles.year{year}.day{day:02d}.part1")
    part2 = importlib.import_module(f"aoc.puzzles.year{year}.day{day:02d}.part2")

    puzzle_input = read_puzzle_input(year, day)

    # Run part 1
    with timer() as t1:
        answer1 = part1.solve(puzzle_input)

    # Run part 2
    with timer() as t2:
        answer2 = part2.solve(puzzle_input)

    return SolveResult(
        year=year,
        day=day,
        part1_answer=answer1,
        part1_time=t1[0],
        part2_answer=answer2,
        part2_time=t2[0],
    )


def run_year(year: int) -> list[SolveResult]:
    """Run all available puzzles for a year.

    Args:
        year: Year to run puzzles for

    Returns:
        List of SolveResults, one per completed day

    """
    results: list[SolveResult] = []
    year_dir = Path(f"aoc/puzzles/year{year}")

    if not year_dir.exists():
        return results

    # Find all day directories
    for day_dir in sorted(year_dir.glob("day*")):
        day = int(day_dir.name[3:])  # Extract day number from "day01"

        # Check if both part1.py and part2.py exist
        if (day_dir / "part1.py").exists() and (day_dir / "part2.py").exists():
            try:
                result = run_day(year, day)
                results.append(result)
                p1, p2 = result.part1_answer, result.part2_answer
                print(f"✓ Day {day:2d}: Part 1 = {p1}, Part 2 = {p2}")
            except (ImportError, AttributeError, FileNotFoundError) as e:
                print(f"✗ Day {day:2d}: Failed - {e}")

    return results


def display_result_table(results: list[SolveResult]) -> None:
    """Display results in formatted table.

    Args:
        results: List of solve results to display

    """
    if not results:
        return

    year = results[0].year
    print(f"\n┌{'─' * 78}┐")
    print(f"│ Year: {year}{' ' * (72 - len(str(year)))}│")
    print(f"├{'─' * 5}┬{'─' * 17}┬{'─' * 17}┬{'─' * 17}┬{'─' * 17}┤")
    print(
        f"│ {'Day':^3} │ {'Part 1 Answer':^15} │ {'Part 2 Answer':^15} │ "
        f"{'Part 1 Time':^15} │ {'Part 2 Time':^15} │"
    )
    print(f"├{'─' * 5}┼{'─' * 17}┼{'─' * 17}┼{'─' * 17}┼{'─' * 17}┤")

    for result in results:
        p1_ans = str(result.part1_answer) if result.part1_answer is not None else "-"
        p2_ans = str(result.part2_answer) if result.part2_answer is not None else "-"
        p1_time = f"{result.part1_time:.3f}s" if result.part1_time > 0 else "-"
        p2_time = f"{result.part2_time:.3f}s" if result.part2_time > 0 else "-"

        print(
            f"│ {result.day:3d} │ {p1_ans:^15} │ {p2_ans:^15} │ "
            f"{p1_time:^15} │ {p2_time:^15} │"
        )

    print(f"└{'─' * 5}┴{'─' * 17}┴{'─' * 17}┴{'─' * 17}┴{'─' * 17}┘\n")
