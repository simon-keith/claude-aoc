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

   The session cookie is already hardcoded in `src/aoc/http.py`, but you can override it with the environment variable.

   To get your session cookie:
   - Log in to [adventofcode.com](https://adventofcode.com)
   - Open browser dev tools (F12)
   - Go to Application/Storage → Cookies
   - Copy the value of the `session` cookie

## Usage

### Solve a Single Day

Use the `/aoc` slash command in Claude Code:

```bash
/aoc 2015 8
```

This will:
1. Wipe any existing solution (clean slate)
2. Download the puzzle and input
3. Interpret the puzzle naturally
4. Generate solution templates with proper structure
5. Create tests from puzzle examples
6. Implement the solution using TDD
7. Submit answers and handle responses
8. Generate markdown documentation
9. Display results in a formatted table
10. Commit everything to git

### Run Tests

```bash
# All tests
pytest

# Specific day
pytest tests/puzzles/test_2015_day08.py

# Just puzzle tests
pytest tests/puzzles/
```

### Run a Solution Manually

```bash
# Run part 1
python puzzles/2015/day08/part1.py

# Run part 2
python puzzles/2015/day08/part2.py
```

## Project Structure

```
claude-aoc/
├── .claude/
│   └── commands/
│       └── aoc.md                   # Slash command with agent workflow
├── src/
│   └── aoc/
│       ├── types.py                 # SolveResult dataclass
│       ├── http.py                  # HTTP client for AoC API
│       ├── helpers.py               # Utility functions
│       └── cli.py                   # CLI interface
├── puzzles/
│   └── {year}/
│       └── day{day:02d}/
│           ├── input.txt            # Puzzle input (committed)
│           ├── part1.py             # Part 1 solution
│           ├── part2.py             # Part 2 solution
│           └── puzzle.md            # Full puzzle documentation
└── tests/
    └── puzzles/
        └── test_{year}_day{day:02d}.py
```

## How It Works

The `/aoc` command triggers a Claude Code agent that follows a comprehensive workflow:

1. **Clean Slate**: Deletes existing puzzle directory for fresh start
2. **Download**: Fetches puzzle HTML and input data
3. **Interpret**: Uses LLM understanding to extract problem details and examples
4. **Generate**: Creates properly structured solution templates
5. **Test**: Writes pytest tests based on examples
6. **Implement**: Solves using TDD methodology
7. **Submit**: Posts answers and interprets responses naturally
8. **Document**: Generates markdown with full puzzle and solutions
9. **Display**: Shows results table with answers and timing

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

## Tips

- **Trust the Examples**: Always make example tests pass before trying real input
- **Part 2 Optimization**: Often needs a completely different algorithm
- **Natural Interpretation**: The agent reads HTML naturally - no need for rigid parsers
- **Clean Slate**: Re-running wipes everything, so you can try different approaches

## License

MIT
