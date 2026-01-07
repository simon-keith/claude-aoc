"""Advent of Code 2016 - Day 11 - Part 1.

Find minimum steps to move all items to floor 4 using BFS.
"""

import re
from collections import deque
from itertools import combinations
from typing import NamedTuple


class State(NamedTuple):
    """Represents a state in the search space."""

    elevator: int  # Current floor (0-3 for floors 1-4)
    # (generator_floor, microchip_floor) for each element
    items: tuple[tuple[int, int], ...]


def parse_input(puzzle_input: str) -> State:  # noqa: C901
    """Parse puzzle input into initial state.

    Args:
        puzzle_input: Raw puzzle input string

    Returns:
        Initial state with elevator at floor 0 and item positions

    """
    lines = puzzle_input.strip().split("\n")
    floors: dict[int, list[tuple[str, str]]] = {0: [], 1: [], 2: [], 3: []}

    for floor_idx, line in enumerate(lines):
        # Find generators
        generators = re.findall(r"(\w+) generator", line)
        for elem in generators:
            floors[floor_idx].append((elem, "G"))

        # Find microchips
        microchips = re.findall(r"(\w+)-compatible microchip", line)
        for elem in microchips:
            floors[floor_idx].append((elem, "M"))

    # Build element list
    elements = set()
    for floor_items in floors.values():
        for elem, _ in floor_items:
            elements.add(elem)

    # Create state tuple: for each element, store (gen_floor, chip_floor)
    element_list = sorted(elements)
    items = []
    for elem in element_list:
        gen_floor = -1
        chip_floor = -1
        for floor_idx in range(4):
            for item_elem, item_type in floors[floor_idx]:
                if item_elem == elem:
                    if item_type == "G":
                        gen_floor = floor_idx
                    else:
                        chip_floor = floor_idx
        items.append((gen_floor, chip_floor))

    return State(elevator=0, items=tuple(items))


def is_valid_floor(generators: set[int], microchips: set[int]) -> bool:
    """Check if a floor configuration is valid.

    A microchip is fried if it's on a floor with a generator that's not its own.

    Args:
        generators: Set of element indices with generators on this floor
        microchips: Set of element indices with microchips on this floor

    Returns:
        True if the floor configuration is safe

    """
    if not generators:
        return True  # No generators means all chips are safe

    return all(chip_elem in generators for chip_elem in microchips)


def is_valid_state(state: State) -> bool:
    """Check if a state is valid (no chips get fried).

    Args:
        state: State to validate

    Returns:
        True if state is valid

    """
    for floor_idx in range(4):
        generators = set()
        microchips = set()

        for elem_idx, (gen_floor, chip_floor) in enumerate(state.items):
            if gen_floor == floor_idx:
                generators.add(elem_idx)
            if chip_floor == floor_idx:
                microchips.add(elem_idx)

        if not is_valid_floor(generators, microchips):
            return False

    return True


def get_next_states(state: State) -> list[State]:  # noqa: C901
    """Generate all valid next states from the current state.

    Args:
        state: Current state

    Returns:
        List of valid next states

    """
    next_states = []
    current_floor = state.elevator

    # Get items on current floor
    items_on_floor = []
    for elem_idx, (gen_floor, chip_floor) in enumerate(state.items):
        if gen_floor == current_floor:
            items_on_floor.append(("G", elem_idx))
        if chip_floor == current_floor:
            items_on_floor.append(("M", elem_idx))

    # Try moving 1 or 2 items
    for num_items in [1, 2]:
        for items_to_move in combinations(items_on_floor, num_items):
            # Try moving up and down
            for direction in [-1, 1]:
                new_floor = current_floor + direction
                if new_floor < 0 or new_floor > 3:
                    continue

                # Create new state
                new_items = list(state.items)
                for item_type, elem_idx in items_to_move:
                    gen_floor, chip_floor = new_items[elem_idx]
                    if item_type == "G":
                        new_items[elem_idx] = (new_floor, chip_floor)
                    else:
                        new_items[elem_idx] = (gen_floor, new_floor)

                new_state = State(elevator=new_floor, items=tuple(new_items))

                if is_valid_state(new_state):
                    next_states.append(new_state)

    return next_states


def canonical_state(state: State) -> tuple[int, tuple[tuple[int, int], ...]]:
    """Convert state to canonical form for duplicate detection.

    Since element identities don't matter (only pairs), we can sort pairs.

    Args:
        state: State to canonicalize

    Returns:
        Canonical representation

    """
    return (state.elevator, tuple(sorted(state.items)))


def solve(puzzle_input: str) -> str:
    """Solve part 1.

    Approach:
        Use BFS to find shortest path from initial state to goal state.
        State: elevator floor + all item positions
        Goal: all items on floor 3 (4th floor)
        Validate each state to ensure no chips get fried.

    Args:
        puzzle_input: Raw puzzle input string

    Returns:
        Minimum number of steps

    """
    initial_state = parse_input(puzzle_input)
    goal_items = tuple((3, 3) for _ in initial_state.items)

    queue = deque([(initial_state, 0)])
    visited = {canonical_state(initial_state)}

    while queue:
        state, steps = queue.popleft()

        # Check if we've reached the goal
        if state.items == goal_items:
            return str(steps)

        # Generate next states
        for next_state in get_next_states(state):
            canon = canonical_state(next_state)
            if canon not in visited:
                visited.add(canon)
                queue.append((next_state, steps + 1))

    return "-1"  # No solution found


if __name__ == "__main__":
    from aoc.helpers import read_puzzle_input

    answer = solve(read_puzzle_input(2016, 11))
    print(answer)
