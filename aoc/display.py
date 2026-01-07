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


def _format_answer(answer: int | str | None) -> str:
    """Format an answer for display, wrapping multiline content in code blocks.

    Args:
        answer: Answer (int, str, or None)

    Returns:
        Formatted answer string

    """
    if answer is None:
        return "-"

    ans_str = str(answer)
    if "\n" in ans_str:
        return f"```\n{ans_str}\n```"
    return ans_str


def _calculate_column_widths(
    rows: list[dict[str, str]], headers: list[str]
) -> dict[str, int]:
    """Calculate column widths based on content.

    Args:
        rows: List of row dictionaries
        headers: List of header names

    Returns:
        Dictionary mapping header to column width

    """
    col_widths = {header: len(header) for header in headers}

    for row in rows:
        for header in headers:
            content = row[header]
            if "\n" in content:
                max_line_width = max(len(line) for line in content.split("\n"))
                col_widths[header] = max(col_widths[header], max_line_width)
            else:
                col_widths[header] = max(col_widths[header], len(content))

    return col_widths


def _print_table_row(
    row: dict[str, str], headers: list[str], col_widths: dict[str, int]
) -> None:
    """Print a single table row, handling multiline content.

    Args:
        row: Row data dictionary
        headers: List of header names
        col_widths: Column width dictionary

    """
    # Split multiline content
    row_lines = {header: row[header].split("\n") for header in headers}
    max_lines = max(len(lines) for lines in row_lines.values())

    # Print each line of the row
    for i in range(max_lines):
        line_parts = []
        for header in headers:
            if i < len(row_lines[header]):
                content = row_lines[header][i].ljust(col_widths[header])
            else:
                content = " " * col_widths[header]
            line_parts.append(content)
        print("| " + " | ".join(line_parts) + " |")


def display_result_table(results: list[SolveResult]) -> None:
    """Display results in formatted markdown table.

    Automatically adjusts column widths to fit content.
    Handles multiline answers (e.g., ASCII art) by displaying them in code blocks.

    Args:
        results: List of solve results to display

    """
    if not results:
        return

    year = results[0].year
    print(f"\n# Advent of Code {year} Results\n")

    # Prepare table data
    headers = ["Day", "Part 1 Answer", "Part 2 Answer", "Part 1 Time", "Part 2 Time"]
    rows = []

    for result in results:
        p1_time = f"{result.part1_time:.3f}s" if result.part1_time > 0 else "-"
        p2_time = f"{result.part2_time:.3f}s" if result.part2_time > 0 else "-"

        rows.append({
            "Day": str(result.day),
            "Part 1 Answer": _format_answer(result.part1_answer),
            "Part 2 Answer": _format_answer(result.part2_answer),
            "Part 1 Time": p1_time,
            "Part 2 Time": p2_time,
        })

    # Calculate column widths and print table
    col_widths = _calculate_column_widths(rows, headers)

    header_row = "| " + " | ".join(
        header.ljust(col_widths[header]) for header in headers
    ) + " |"
    separator = "| " + " | ".join("-" * col_widths[header] for header in headers) + " |"

    print(header_row)
    print(separator)

    for row in rows:
        _print_table_row(row, headers, col_widths)

    print()
