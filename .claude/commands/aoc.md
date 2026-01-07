---
description: Solve Advent of Code puzzles
argument-hint: [year] [day]
---

# Advent of Code Solver

Solves Advent of Code puzzles using automated TDD workflow. When the user runs `/aoc <year> <day>`, follow these steps:

## Common Commands

### Fetch Puzzle HTML
```bash
uv run python -c "
from aoc.http import AoCClient
client = AoCClient()
html = client.fetch_puzzle(year, day)
print(html)"
```

### Interpreting Puzzle HTML
When you receive puzzle HTML:
- Read and understand the HTML content directly (don't write HTML parsers or use BeautifulSoup)
- **Extract key information**: puzzle title, part description, example inputs with their expected outputs
- **If already solved**: Look for answer values in `<p>` tags after the `<article>` section (e.g., "Your puzzle answer was `12345`")

**Note**: All Python commands that use project dependencies must be run with `uv run` to ensure the virtual environment is active.

## Workflow

### 1. Clean Slate
Delete the puzzle directory if it exists:
```bash
uv run python -c "from aoc.helpers import wipe_puzzle; wipe_puzzle(year, day)"
```

### 2. Download Input
Download the puzzle input file:
```bash
uv run python -c "
from aoc.http import AoCClient
from aoc.helpers import ensure_puzzle_dir

client = AoCClient()
puzzle_dir = ensure_puzzle_dir(year, day)
(puzzle_dir / 'input.txt').write_text(client.fetch_input(year, day))"
```

### 3. Fetch & Interpret Puzzle
Use the [Fetch Puzzle HTML](#fetch-puzzle-html) command, then follow [Interpreting Puzzle HTML](#interpreting-puzzle-html) guidance to extract Part 1 information.

### 4. Generate Part 1

Create `aoc/puzzles/year{year}/day{day:02d}/part1.py`:

```python
"""Advent of Code {year} - Day {day} - Part 1.

{Brief 1-sentence description}
"""


def solve(puzzle_input: str) -> str:
    """Solve part 1.

    Approach:
        {Describe solution approach}

    Args:
        puzzle_input: Raw puzzle input string

    Returns:
        The answer to part 1

    """
    # TODO: Implement
    return "0"


if __name__ == "__main__":
    from aoc.helpers import read_puzzle_input

    answer = solve(read_puzzle_input({year}, {day}))
    print(answer)
```

### 5. Generate Part 1 Tests

Create `tests/puzzles/test_{year}_day{day:02d}.py`:

```python
"""Tests for Advent of Code {year} Day {day}."""

from aoc.puzzles.year{year}.day{day:02d} import part1


class TestPart1:
    def test_example_1(self):
        """Test with {description}."""
        assert part1.solve("{example_input}") == {expected_output}

    def test_example_2(self):
        """Test with {description}."""
        assert part1.solve("{example_input}") == {expected_output}
```

**Notes**:
- Create one test per example from the puzzle
- Simply pass test input directly to `solve()` - no mocking needed!
- Tests don't need docstrings or type annotations (ruff exemptions apply)
- For multi-line inputs, use triple-quoted strings or `\n` in test data

### 6. Implement Part 1 (TDD Approach)

Follow this methodology:

1. **Analyze & Extract**: Read the problem description and separate the narrative from the technical constraints. Identify exactly what the output should be.

2. **Parsing Strategy**: Analyze the input format. Design the data structures you'll need (lists, dicts, sets, grids, graphs, etc.). Write parsing code.

3. **Validate with Examples**: Run pytest on your tests. **Make the example tests pass FIRST** before trying the real input. This is critical!

4. **Implement Solution**: Once examples pass, implement the full algorithm for the real input.

5. **Iterate**: If tests fail, debug and fix. The examples are your contract.

6. **Debug & Polish**:
   - Use `print()` statements for debugging during development
   - Remove debug prints before finalizing solution


### 7. Run Part 1 on Real Input

Run the file as a module: `uv run python -m aoc.puzzles.year{year}.day{day:02d}.part1`

This will execute the `if __name__ == "__main__"` block which prints the answer.

### 8. Submit Part 1

Submit the answer:
```bash
uv run python -c "
from aoc.http import AoCClient
client = AoCClient()
response = client.submit_answer(year, day, 1, 'answer')
print(response)"
```

Interpret response naturally:
- **"That's the right answer"** → ✅ Success, continue to Part 2
- **"Did you already complete it?"** → ✅ Extract answer from response, verify code matches
- **"You gave an answer too recently"** → ⏸️ Wait specified time, retry
- **"too high"/"too low"** → ❌ Add constraint to tests, fix implementation, retry

### 9. Fetch Part 2
Use the [Fetch Puzzle HTML](#fetch-puzzle-html) command (now includes Part 2), then follow [Interpreting Puzzle HTML](#interpreting-puzzle-html) to extract Part 2 information.

### 10. Generate Part 2

Create `aoc/puzzles/year{year}/day{day:02d}/part2.py`:

```python
"""Advent of Code {year} - Day {day} - Part 2.

{Brief 1-sentence description}
"""


def solve(puzzle_input: str) -> str:
    """Solve part 2.

    Approach:
        {Describe approach}
        {Note if reusing part1 or new algorithm}

    Args:
        puzzle_input: Raw puzzle input string

    Returns:
        The answer to part 2

    """
    # Can import: from aoc.puzzles.year{year}.day{day:02d} import part1
    return "0"


if __name__ == "__main__":
    from aoc.helpers import read_puzzle_input

    answer = solve(read_puzzle_input({year}, {day}))
    print(answer)
```

### 11. Add Part 2 Tests

Add to existing `tests/puzzles/test_{year}_day{day:02d}.py`:

```python
from aoc.puzzles.year{year}.day{day:02d} import part1, part2  # Update import


class TestPart2:
    def test_example_1(self):
        """Test with {description}."""
        assert part2.solve("{example_input}") == {expected_output}
```

### 12. Implement Part 2
- Follow same TDD methodology as Part 1
- **Important**: Part 2 often requires algorithmic improvements (dynamic programming, memoization, mathematical formulas, graph algorithms, etc.)
- Make tests pass before running on real input

### 13. Submit Part 2
- Same process as Part 1

### 14. Generate puzzle.md
Generate the puzzle documentation:
```bash
uv run python -c "
from aoc.http import AoCClient
from aoc.helpers import save_puzzle_markdown

client = AoCClient()
html = client.fetch_puzzle(year, day)
puzzle_path = save_puzzle_markdown(html, year, day)
print(f'Generated {puzzle_path}')"
```

This extracts title, descriptions, answers, and saves to `aoc/puzzles/year{year}/day{day:02d}/puzzle.md`.

### 15. Display Results

Run and display a single day:
```bash
uv run python -c "
from aoc.display import run_day, display_result_table

result = run_day(year, day)
display_result_table([result])"
```

Or run all completed days for a year:
```bash
uv run python -c "
from aoc.display import run_year, display_result_table

results = run_year(year)
display_result_table(results)"
```

### 16. Report Improvements (Optional)

If you encountered workflow issues, helper bugs, unclear instructions, or opportunities for improvement, report them briefly to help refine the process for future puzzles.

## Standards & Constraints

### Code Quality
- Use type annotations on all functions
- Add docstrings explaining your approach
- Add comments for non-obvious logic
- Use meaningful variable names (avoid `data`, `result`, `temp`, `info`)
- Apply Occam's Razor - remove unnecessary complexity
- Don't suppress linter warnings (`# noqa`, `# type: ignore`) without documented reason
- Validate with: `uv run ruff check aoc/puzzles/year{year}/day{day:02d}/` and `uv run mypy aoc/puzzles/year{year}/day{day:02d}/`

### Performance
- Aim for solutions that run under 1 second when possible
- 10 seconds is the absolute maximum - if a solution takes longer, ask the user for guidance on optimization strategies or acceptable trade-offs

### General Constraints
- **Pure Python only** - standard library only, no numpy/pandas/external packages
- **TDD always** - validate examples before real input (saves submission attempts)
- **No cheating** - solve yourself, don't search for solutions online
- **No git commits** - user will commit when ready
