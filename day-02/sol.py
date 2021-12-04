#!/usr/bin/env python3

import typing as t


Instructions = t.Sequence[t.Tuple[str, int]]


def parse_input(input: str) -> Instructions:
    instructions = []
    for line in input.splitlines():
        op, val = line.split(sep=None, maxsplit=1)
        instructions.append((op, int(val)))
    return instructions


def part1(instructions: Instructions) -> int:
    hpos = 0
    depth = 0
    for (op, val) in instructions:
        if op == "forward":
            hpos += val
        else:
            val *= (op == "down") * 2 - 1
            depth += val
    return hpos * depth


def part2(instructions: Instructions) -> int:
    hpos = 0
    depth = 0
    aim = 0
    for (op, val) in instructions:
        if op == "forward":
            hpos += val
            depth += aim * val
        else:
            val *= (op == "down") * 2 - 1
            aim += val
    return hpos * depth


example_input = parse_input("""\
forward 5
down 5
forward 8
up 3
down 8
forward 2""")
print(part1(example_input), 150)
print(part2(example_input), 900)

my_input = parse_input(open("input.txt").read())
print(part1(my_input), 1561344)
print(part2(my_input), 1848454425)
