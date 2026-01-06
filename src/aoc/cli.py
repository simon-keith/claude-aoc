"""Command-line interface for the AoC solver."""

import sys

from aoc.types import SolveResult


def main() -> None:
    """Entry point for CLI.

    Usage:
        python -m aoc.cli <year> <day>
    """
    if len(sys.argv) < 3:
        print("Usage: python -m aoc.cli <year> <day>")
        sys.exit(1)

    year = int(sys.argv[1])
    day = int(sys.argv[2])

    print(f"🎄 Starting Advent of Code solver for {year} day {day}")
    print()
    print("The Claude Code agent will now follow the workflow defined in:")
    print("  .claude/commands/aoc.md")
    print()
    print("Workflow steps:")
    print("  1. Wipe existing puzzle directory (clean slate)")
    print("  2. Download input.txt")
    print("  3. Fetch and interpret puzzle HTML")
    print("  4. Generate part1.py template")
    print("  5. Write tests based on examples")
    print("  6. Implement part 1 using TDD")
    print("  7. Run and time part 1")
    print("  8. Submit answer for part 1")
    print("  9. Fetch updated HTML (with part 2)")
    print(" 10. Generate part2.py template")
    print(" 11. Implement part 2 using TDD")
    print(" 12. Submit answer for part 2")
    print(" 13. Generate puzzle.md documentation")
    print(" 14. Display results and commit to git")
    print()


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


if __name__ == "__main__":
    main()
