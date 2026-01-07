"""Advent of Code 2016 - Day 12 - Part 1.

Execute assembunny code and return value in register a.
"""


def execute(instructions: list[str], registers: dict[str, int]) -> dict[str, int]:
    """Execute assembunny instructions.

    Args:
        instructions: List of instruction strings
        registers: Initial register values

    Returns:
        Final register values

    """
    pc = 0  # Program counter

    def get_value(operand: str) -> int:
        """Get value of operand (register or integer)."""
        if operand.lstrip("-").isdigit():
            return int(operand)
        return registers[operand]

    while 0 <= pc < len(instructions):
        parts = instructions[pc].split()
        op = parts[0]

        if op == "cpy":
            value = get_value(parts[1])
            registers[parts[2]] = value
            pc += 1
        elif op == "inc":
            registers[parts[1]] += 1
            pc += 1
        elif op == "dec":
            registers[parts[1]] -= 1
            pc += 1
        elif op == "jnz":
            value = get_value(parts[1])
            if value != 0:
                pc += int(parts[2])
            else:
                pc += 1

    return registers


def solve(puzzle_input: str) -> str:
    """Solve part 1.

    Approach:
        Implement an interpreter for assembunny code with
        4 registers and 4 instructions: cpy, inc, dec, jnz.
        Execute until program halts, then return value in register a.

    Args:
        puzzle_input: Raw puzzle input string

    Returns:
        Value in register a after execution

    """
    instructions = puzzle_input.strip().split("\n")
    registers = {"a": 0, "b": 0, "c": 0, "d": 0}

    result = execute(instructions, registers)
    return str(result["a"])


if __name__ == "__main__":
    from aoc.helpers import read_puzzle_input

    answer = solve(read_puzzle_input(2016, 12))
    print(answer)
