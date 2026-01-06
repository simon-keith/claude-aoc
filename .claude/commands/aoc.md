---
description: Solve Advent of Code puzzles
argument-hint: [year] [day]
---

# Advent of Code Solver

Solves Advent of Code puzzles using an automated TDD workflow.

## Usage

When the user runs `/aoc <year> <day>`, follow this complete workflow to solve both parts of the puzzle.

## Complete Workflow

### Step 1: Clean Slate

- Check if `puzzles/{year}/day{day:02d}/` exists
- If yes: **DELETE the entire directory** using `wipe_puzzle(year, day)` from helpers
- This ensures a completely fresh implementation attempt

### Step 2: Download Input

- Use `AoCClient().fetch_input(year, day)` to download the input data
- Save to `puzzles/{year}/day{day:02d}/input.txt`
- Create the directory if it doesn't exist using `ensure_puzzle_dir(year, day)`
- **This file will be committed to git**

### Step 3: Fetch & Interpret Puzzle HTML

- Use WebFetch or `AoCClient().fetch_puzzle(year, day)` to get the puzzle HTML
- **Read and understand the HTML naturally** - you're an LLM, don't write parsers!
- Extract by understanding the content:
  - Puzzle title (in `<h2>`)
  - Part 1 description (first `<article class="day-desc">`)
  - Examples with their inputs and expected outputs
  - If already solved: answers appear in `<p>` tags right after the `<article>`
  - Part 2 (if visible): second `<article class="day-desc">`)

**Important**: Examples may be in `<pre><code>` blocks, inline in text, or in various formats. Use your understanding to extract them - don't rely on rigid HTML parsing.

### Step 4: Generate Part 1 Template

Create `puzzles/{year}/day{day:02d}/part1.py` with this structure:

```python
"""Advent of Code {year} - Day {day} - Part 1.

{Brief 1-sentence description of the problem}
"""
from pathlib import Path


def solve() -> int | str:
    """Solve part 1.

    Approach:
        {Describe your solution approach here}

    Returns:
        The answer to part 1
    """
    input_data = read_input()
    # TODO: Implement solution
    return 0


def read_input() -> str:
    """Read and return the input file contents.

    Returns:
        Raw input text with trailing whitespace stripped
    """
    return (Path(__file__).parent / "input.txt").read_text().strip()


if __name__ == "__main__":
    answer = solve()
    print(f"Part 1: {answer}")
```

### Step 5: Generate Tests

- Create `tests/puzzles/test_{year}_day{day:02d}.py`
- Write pytest tests based on the examples you extracted from the HTML
- One test per example
- Mock the `read_input()` function or create test helper functions
- Tests don't need docstrings or annotations (ruff exemptions apply)

Example test structure:

```python
import sys
from pathlib import Path

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "src"))

from puzzles.{year}.day{day:02d} import part1


def test_part1_example1():
    # Override read_input to return example
    original = part1.read_input
    part1.read_input = lambda: "{example_input}"

    result = part1.solve()
    assert result == {expected_output}

    part1.read_input = original
```

### Step 6: Implement Part 1 (TDD Approach)

Follow the user's specified problem-solving methodology:

1. **Analyze & Extract**: Read the problem description and separate the narrative from the technical constraints. Identify exactly what the output should be.

2. **Parsing Strategy**: Analyze the input format. Design the data structures you'll need (lists, dicts, sets, grids, graphs, etc.). Write parsing code.

3. **Validate with Example**: Run pytest on your tests. **Make the example tests pass FIRST** before trying the real input. This is critical!

4. **Implement Solution**: Once examples pass, implement the full algorithm for the real input.

5. **Iterate**: If tests fail, debug and fix. The examples are your contract.

**Code Quality Requirements**:
- Use type annotations on all functions
- Add docstrings explaining your approach
- Add comments for non-obvious logic
- Code must pass `ruff check` and `mypy`

### Step 7: Run Part 1 on Real Input

- Import the module: `from puzzles.{year}.day{day:02d} import part1`
- Use the `timer()` context manager from helpers:
  ```python
  from aoc.helpers import timer

  with timer() as t:
      answer = part1.solve()

  part1_time = t[0]
  ```
- Record the answer and time

### Step 8: Submit Part 1 Answer

- Use `AoCClient().submit_answer(year, day, 1, answer)` to submit
- Read the HTML response **naturally** - interpret it as text, don't write a parser!
- Look for these phrases and interpret accordingly:

**"That's the right answer"**
- ✅ Success! Part 1 is complete.
- Proceed to Step 9

**"Did you already complete it?"**
- ✅ Already solved previously
- The response contains the correct answer in text like "your puzzle answer was X"
- Extract this answer from the text
- Verify your code produces this answer
- If not, fix your implementation
- Proceed to Step 9

**"You gave an answer too recently"**
- ⏸️ Rate limited
- The response contains wait time like "You have 5m 23s left to wait"
- Extract the wait time
- Display it to the user
- Wait the specified time, then retry submission

**"That's not the right answer"**
- ❌ Wrong answer
- Check if response contains "too high" → answer is too high
- Check if response contains "too low" → answer is too low
- Otherwise → just wrong
- Go back to Step 6
- Add constraints to your tests based on the hint (e.g., `assert result < wrong_answer`)
- Fix your implementation
- Retry

### Step 9: Fetch Updated Puzzle HTML (Part 2 Unlocked)

- **Fetch HTML again**: `AoCClient().fetch_puzzle(year, day)`
- The HTML has now changed! It now contains:
  - Part 1 description with the correct answer
  - Part 2 description (newly visible!)
  - Part 2 examples (if any)
- Extract Part 2 information using natural language understanding

### Step 10: Generate Part 2 Template

Create `puzzles/{year}/day{day:02d}/part2.py`:

```python
"""Advent of Code {year} - Day {day} - Part 2.

{Brief 1-sentence description of part 2}
"""
from pathlib import Path

from . import part1  # Can reuse part1 code


def solve() -> int | str:
    """Solve part 2.

    Approach:
        {Describe your solution approach here}
        {Note if you're reusing part1 logic or need a new algorithm}

    Returns:
        The answer to part 2
    """
    input_data = read_input()
    # TODO: Implement solution
    # Can call part1 functions if useful
    return 0


def read_input() -> str:
    """Read and return the input file contents.

    Returns:
        Raw input text with trailing whitespace stripped
    """
    return (Path(__file__).parent / "input.txt").read_text().strip()


if __name__ == "__main__":
    answer = solve()
    print(f"Part 2: {answer}")
```

### Step 11: Implement Part 2

- Add Part 2 tests to `tests/puzzles/test_{year}_day{day:02d}.py`
- Follow the same TDD methodology as Part 1
- **Important**: Part 2 often requires a different algorithm or optimization
  - If Part 1 runs in milliseconds but Part 2 needs millions of iterations, you need a better algorithm
  - Consider: dynamic programming, memoization, mathematical formulas, graph algorithms, etc.
- Make sure tests pass before running on real input
- Must pass ruff and mypy

### Step 12: Submit Part 2 Answer

- Same process as Step 8
- Submit, interpret response naturally, retry if needed
- Handle all response types the same way

### Step 13: Generate Final Markdown Documentation

- **Fetch HTML one final time**: The page now shows both parts with both answers
- Convert the puzzle to markdown and save as `puzzles/{year}/day{day:02d}/puzzle.md`
- Include in the markdown:
  - Puzzle title
  - Full Part 1 description
  - Part 1 solution code (read from part1.py)
  - Part 1 answer and execution time
  - Full Part 2 description
  - Part 2 solution code (read from part2.py)
  - Part 2 answer and execution time

### Step 14: Display Results & Commit

- Create a `SolveResult` object:
  ```python
  from aoc.types import SolveResult

  result = SolveResult(
      year=year,
      day=day,
      part1_answer=part1_answer,
      part1_time=part1_time,
      part2_answer=part2_answer,
      part2_time=part2_time,
  )
  ```

- Display using the table formatter:
  ```python
  from aoc.cli import display_result_table

  display_result_table([result])
  ```

- Commit to git:
  ```bash
  git add puzzles/{year}/day{day:02d}/
  git add tests/puzzles/test_{year}_day{day:02d}.py
  git commit -m "Solve AoC {year} day {day}

  Part 1: {part1_answer} ({part1_time:.3f}s)
  Part 2: {part2_answer} ({part2_time:.3f}s)"
  ```

## Important Reminders

- **Pure Python Only**: Solutions use ONLY the standard library. No numpy, pandas, or external packages.
- **Natural Language Interpretation**: Don't write HTML parsers. Read and understand HTML as text.
- **TDD Always**: Validate with examples before running on real input. This saves submission attempts.
- **Code Quality**: All solutions must have type annotations, docstrings, and pass ruff/mypy.
- **Documentation**: Explain your approach in docstrings so others can understand your solution.
- **Optimization**: Part 2 often requires algorithmic improvements, not just running the same code.
- **NO CHEATING**: You are STRICTLY FORBIDDEN from searching for solutions online. This includes:
  - DO NOT use WebSearch to look for Advent of Code solutions
  - DO NOT search on r/adventofcode subreddit or any forum
  - DO NOT look up solutions on GitHub, blogs, or solution repositories
  - DO NOT use WebFetch to access solution websites
  - You MUST solve the puzzle yourself using ONLY the problem description and examples provided
  - The goal is to develop your own algorithmic solution, not to copy someone else's work

## Available Helper Functions

From `aoc.helpers`:
- `get_puzzle_dir(year, day)` - Get puzzle directory path
- `ensure_puzzle_dir(year, day)` - Create puzzle directory
- `wipe_puzzle(year, day)` - Delete puzzle directory for fresh start
- `timer()` - Context manager for timing code blocks

From `aoc.http`:
- `AoCClient().fetch_puzzle(year, day)` - Get puzzle HTML
- `AoCClient().fetch_input(year, day)` - Get input data
- `AoCClient().submit_answer(year, day, part, answer)` - Submit answer

From `aoc.cli`:
- `display_result_table(results)` - Display formatted results table

## Session Cookie

The session cookie is already configured in `src/aoc/http.py`. It falls back to the `AOC_SESSION` environment variable if set.
