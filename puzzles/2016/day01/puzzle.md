# Day 1: No Time for a Taxicab

## Part 1

You're airdropped just outside of Easter Bunny Headquarters in a city somewhere. The city's streets form a perfect grid, and you start at the origin, facing North.

Following a sequence of instructions (like R2, L3 meaning "turn right, walk 2 blocks, then turn left, walk 3 blocks"), you need to determine the shortest path to your destination.

The instructions consist of a sequence of turns (L for left, R for right) followed by a number of blocks to walk forward in that direction.

**Examples:**
- `R2, L3` leaves you 2 blocks East and 3 blocks North, or 5 blocks away
- `R2, R2, R2` leaves you 2 blocks South of where you started, or 2 blocks away
- `R5, L5, R5, R3` leaves you 12 blocks away

**Question:** How many blocks away is Easter Bunny HQ?

### Solution

```python
"""Advent of Code 2016 - Day 1 - Part 1.

No Time for a Taxicab: Calculate Manhattan distance to destination.
"""
from pathlib import Path


def solve() -> int:
    """Solve part 1.

    Approach:
        Track position (x, y) and facing direction
        Parse each instruction (turn + distance)
        Update direction based on turn (L/R)
        Move forward in current direction
        Return Manhattan distance from origin

    Returns:
        Manhattan distance to final position
    """
    instructions = read_input().split(", ")

    # Starting position and direction
    x, y = 0, 0
    # Direction: 0=North, 1=East, 2=South, 3=West
    direction = 0

    # Direction vectors: North, East, South, West
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    for instruction in instructions:
        turn = instruction[0]
        distance = int(instruction[1:])

        # Update direction
        if turn == 'R':
            direction = (direction + 1) % 4
        else:  # L
            direction = (direction - 1) % 4

        # Move forward
        x += dx[direction] * distance
        y += dy[direction] * distance

    # Manhattan distance
    return abs(x) + abs(y)


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

**Answer:** 161
**Execution Time:** ~0.000s

## Part 2

Then, you notice the instructions continue on the back of the Recruiting Document. Easter Bunny HQ is actually at the first location you visit twice.

For example, if your instructions are `R8, R4, R4, R8`, the first location you visit twice is 4 blocks away, due East.

**Question:** How many blocks away is the first location you visit twice?

### Solution

```python
"""Advent of Code 2016 - Day 1 - Part 2.

Find the first location visited twice.
"""
from pathlib import Path


def solve() -> int:
    """Solve part 2.

    Approach:
        Track all visited positions as we move
        For each step, record every position along the path (not just endpoints)
        Return Manhattan distance to first position visited twice

    Returns:
        Manhattan distance to first repeated position
    """
    instructions = read_input().split(", ")

    # Starting position and direction
    x, y = 0, 0
    # Direction: 0=North, 1=East, 2=South, 3=West
    direction = 0

    # Direction vectors: North, East, South, West
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    # Track all visited positions
    visited = {(0, 0)}

    for instruction in instructions:
        turn = instruction[0]
        distance = int(instruction[1:])

        # Update direction
        if turn == 'R':
            direction = (direction + 1) % 4
        else:  # L
            direction = (direction - 1) % 4

        # Move forward one block at a time, checking each position
        for _ in range(distance):
            x += dx[direction]
            y += dy[direction]

            # Check if we've been here before
            if (x, y) in visited:
                # Found first repeated location!
                return abs(x) + abs(y)

            visited.add((x, y))

    # Should not reach here based on puzzle description
    return -1


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

**Answer:** 110
**Execution Time:** ~0.000s

---

**Both parts completed successfully!** ⭐⭐
