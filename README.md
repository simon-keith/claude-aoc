# Claude AoC Solver

An Advent of Code puzzle solver powered by Claude Code, featuring automated TDD workflows and natural language understanding.

## Features

- **Agent-Driven Solving**: Claude Code agent interprets puzzles naturally without rigid HTML parsing
- **TDD Workflow**: Automatically extracts examples, generates tests, and validates solutions before submission
- **Clean Slate**: Re-running a puzzle wipes everything for fresh implementation
- **Pure Python**: All solutions use only the Python standard library
- **Code Quality**: Solutions include full type annotations, docstrings, and pass ruff/mypy validation
- **Performance Tracking**: Measure and display execution times for each part

## Setup

1. **Clone and install**:
   ```bash
   git clone <your-repo>
   cd claude-aoc
   uv sync
   ```

2. **Set your session cookie** (optional - already configured):
   ```bash
   export AOC_SESSION="your_session_cookie_here"
   ```

   The session cookie is already hardcoded in `aoc/http.py`, but you can override it with the environment variable.

   To get your session cookie:
   - Log in to [adventofcode.com](https://adventofcode.com)
   - Open browser dev tools (F12)
   - Go to Application/Storage → Cookies
   - Copy the value of the `session` cookie

## Usage

### Solve a Single Day

Use the `/aoc` slash command in Claude Code:

```bash
/aoc 2016 8
```

This will:
1. Wipe any existing solution and tests (clean slate)
2. Download the puzzle and input
3. Interpret the puzzle naturally
4. Generate solution templates with proper structure
5. Create tests from puzzle examples
6. Implement the solution using TDD
7. Submit answers and handle responses
8. Generate markdown documentation
9. Display results in a formatted table

**Note**: The workflow does NOT automatically commit to git. You should review and commit changes when ready.

### Run Tests

```bash
# All tests
uv run pytest

# Specific day
uv run pytest tests/puzzles/test_2016_day08.py

# Just puzzle tests
uv run pytest tests/puzzles/

# With verbose output
uv run pytest tests/puzzles/ -v
```

### Run a Solution Manually

```bash
# Run part 1
uv run python aoc/puzzles/year2016/day08/part1.py

# Run part 2
uv run python aoc/puzzles/year2016/day08/part2.py
```

### Display Results for a Year

```python
# Show all completed puzzles for a year with timing
uv run python -c "
from aoc.display import run_year, display_result_table
results = run_year(2016)
display_result_table(results)
"
```

## Project Structure

```
claude-aoc/
├── .claude/
│   └── commands/
│       └── aoc.md                          # Slash command with agent workflow
├── aoc/                                     # Main package (no longer in src/)
│   ├── types.py                            # SolveResult dataclass
│   ├── http.py                             # HTTP client for AoC API
│   ├── helpers.py                          # Utility functions (wipe_puzzle, read_input, etc.)
│   ├── display.py                          # Results table formatting with markdown
│   └── puzzles/
│       └── year{year}/
│           └── day{day:02d}/
│               ├── __init__.py             # Optional package marker
│               ├── input.txt               # Puzzle input (committed)
│               ├── part1.py                # Part 1 solution
│               ├── part2.py                # Part 2 solution
│               └── puzzle.md               # Full puzzle documentation
└── tests/
    └── puzzles/
        └── test_{year}_day{day:02d}.py     # Pytest tests for both parts
```

## How It Works

The `/aoc` command triggers a Claude Code agent that follows a comprehensive workflow (documented in [.claude/commands/aoc.md](.claude/commands/aoc.md)):

1. **Clean Slate**: Deletes existing puzzle directory and test files for fresh start
2. **Download**: Fetches puzzle HTML and input data
3. **Interpret**: Uses LLM understanding to extract problem details and examples
4. **Generate**: Creates properly structured solution templates in `aoc/puzzles/year{year}/day{day:02d}/`
5. **Test**: Writes pytest tests in `tests/puzzles/` based on examples
6. **Implement**: Solves using TDD methodology
7. **Submit**: Posts answers and interprets responses naturally
8. **Document**: Generates `puzzle.md` with full puzzle description
9. **Display**: Shows results table with answers and timing (optional)

**Important**: The workflow follows a strict anti-cheating policy - no searching for solutions online or looking at other people's code.

### TDD Methodology

The agent follows a rigorous problem-solving approach:

1. **Analyze**: Separate story from technical constraints
2. **Parse Strategy**: Design data structures for input
3. **Validate with Examples**: Make tests pass first!
4. **Solve**: Implement for real input
5. **Optimize**: Part 2 often needs algorithmic improvements

### Code Quality

All solutions must:
- Use only Python standard library (no external dependencies)
- Have full type annotations on all functions
- Include docstrings explaining the approach
- Add comments for non-obvious logic
- Pass `ruff check` and `mypy` validation

## Answer Submission

The agent interprets submission responses naturally:

- ✅ **"That's the right answer"** → Success, proceed to next part
- ✅ **"Did you already complete it"** → Extract answer, verify code matches
- ⏸️ **"You gave an answer too recently"** → Wait the specified time
- ❌ **"too high" / "too low"** → Add constraints, retry

## Special Cases

### Visual/ASCII Art Puzzles

Some puzzles (e.g., 2016 Day 8) produce visual outputs that need manual interpretation:
- Part 2 returns ASCII art directly as a multiline string
- The answer must be read visually from the output
- See [Visual/ASCII Art Handling](.claude/commands/aoc.md#handling-visualascii-art-outputs) in `aoc.md` for details

## Tips

- **Trust the Examples**: Always make example tests pass before trying real input
- **Part 2 Optimization**: Often needs a completely different algorithm
- **Natural Interpretation**: The agent reads HTML naturally - no need for rigid parsers
- **Clean Slate**: Re-running wipes both puzzle files and tests for fresh start
- **Test Coverage**: Ensure both Part 1 and Part 2 have tests before submitting

## License

MIT
