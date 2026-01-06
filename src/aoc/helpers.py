"""Helper utilities for the AoC solver."""

import shutil
import time
from collections.abc import Iterator
from contextlib import contextmanager
from pathlib import Path


def get_puzzle_dir(year: int, day: int) -> Path:
    """Get puzzle directory path.

    Args:
        year: Year of the puzzle
        day: Day of the puzzle (1-25)

    Returns:
        Path to the puzzle directory

    """
    return Path(f"puzzles/{year}/day{day:02d}")


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
    """Delete all puzzle files for fresh start.

    Args:
        year: Year of the puzzle
        day: Day of the puzzle (1-25)

    """
    path = get_puzzle_dir(year, day)
    if path.exists():
        shutil.rmtree(path)


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
