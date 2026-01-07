"""Helper utilities for the AoC solver."""

import re
import shutil
import time
from collections.abc import Iterator
from contextlib import contextmanager
from pathlib import Path

from bs4 import BeautifulSoup
from markdownify import markdownify as md


def get_puzzle_dir(year: int, day: int) -> Path:
    """Get puzzle directory path.

    Args:
        year: Year of the puzzle
        day: Day of the puzzle (1-25)

    Returns:
        Path to the puzzle directory

    """
    return Path(__file__).parent / "puzzles" / f"year{year}" / f"day{day:02d}"


def ensure_puzzle_dir(year: int, day: int) -> Path:
    """Ensure puzzle directory exists.

    Args:
        year: Year of the puzzle
        day: Day of the puzzle (1-25)

    Returns:
        Path to the puzzle directory

    """
    path = get_puzzle_dir(year, day)
    path.mkdir(parents=True, exist_ok=True)
    return path


def wipe_puzzle(year: int, day: int) -> None:
    """Delete all puzzle files and tests for fresh start.

    Args:
        year: Year of the puzzle
        day: Day of the puzzle (1-25)

    """
    path = get_puzzle_dir(year, day)
    if path.exists():
        shutil.rmtree(path)

    # Also delete the test file for this day
    test_path = (
        Path(__file__).parent.parent / "tests" / "puzzles" / f"test_{year}_day{day:02d}.py"
    )
    if test_path.exists():
        test_path.unlink()


def read_puzzle_input(year: int, day: int) -> str:
    """Read puzzle input file.

    Args:
        year: Year of the puzzle
        day: Day of the puzzle (1-25)

    Returns:
        Raw input text with trailing whitespace stripped

    """
    input_path = get_puzzle_dir(year, day) / "input.txt"
    return input_path.read_text().strip()


def generate_puzzle_markdown(html: str, day: int) -> str:
    """Generate puzzle markdown from AoC HTML.

    Args:
        html: Raw HTML from fetch_puzzle()
        day: Day of the puzzle (1-25)

    Returns:
        Formatted markdown content for puzzle.md

    Raises:
        ValueError: If HTML structure doesn't match expected format

    """
    soup = BeautifulSoup(html, "html.parser")

    # Extract title from first h2
    title_tag = soup.find("h2")
    if not title_tag:
        msg = "Could not find puzzle title (h2 tag)"
        raise ValueError(msg)

    # Extract title (e.g., "--- Day 2: Bathroom Security ---" -> "Bathroom Security")
    match = re.match(r"---\s*Day\s*\d+:\s*(.+?)\s*---", title_tag.get_text())
    if not match:
        msg = f"Unexpected title format: {title_tag.get_text()}"
        raise ValueError(msg)
    title = match.group(1)

    # Find article tags (Part 1 and optionally Part 2)
    articles = soup.find_all("article", class_="day-desc")
    if not articles:
        msg = "Could not find any article tags with class 'day-desc'"
        raise ValueError(msg)

    parts = [f"# Day {day}: {title}\n"]

    # Process each article (Part 1, Part 2)
    for i, article in enumerate(articles, 1):
        # Convert article to markdown
        article_md = md(str(article), heading_style="atx")
        # Remove the heading (gets converted to ## by markdownify)
        article_md = re.sub(r"^##\s*---.*?---\s*\n+", "", article_md)

        part_name = "Part One" if i == 1 else "Part Two"
        parts.append(f"\n## {part_name}\n\n{article_md.strip()}\n")

        # Look for answer in next sibling <p> tag
        answer_tag = article.find_next_sibling("p")
        if answer_tag:
            # Extract answer from <code> tag within the <p>
            code_tag = answer_tag.find("code")
            if code_tag:
                answer = code_tag.get_text()
                parts.append(f"\n**Your puzzle answer was `{answer}`.**\n")

    return "\n".join(parts)


def save_puzzle_markdown(html: str, year: int, day: int) -> Path:
    """Generate and save puzzle markdown file.

    Args:
        html: Raw HTML from fetch_puzzle()
        year: Year of the puzzle
        day: Day of the puzzle (1-25)

    Returns:
        Path to the saved puzzle.md file

    """
    markdown = generate_puzzle_markdown(html, day)
    puzzle_dir = ensure_puzzle_dir(year, day)
    puzzle_path = puzzle_dir / "puzzle.md"
    puzzle_path.write_text(markdown)
    return puzzle_path


@contextmanager
def timer() -> Iterator[list[float]]:
    """Time a block of code.

    Yields:
        A list containing a single float (the elapsed time in seconds)

    Example:
        with timer() as t:
            do_something()
        print(f"Took {t[0]:.3f}s")

    """
    start = time.perf_counter()
    elapsed: list[float] = [0.0]
    try:
        yield elapsed
    finally:
        elapsed[0] = time.perf_counter() - start
