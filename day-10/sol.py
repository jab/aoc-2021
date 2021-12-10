#!/usr/bin/env python3

from typing import NamedTuple


closing_by_opening = {"(": ")", "{": "}", "[": "]", "<": ">"}
is_opening = closing_by_opening.__contains__


class Corrupted(NamedTuple):
    expected: str | None
    got: str


class Incomplete(NamedTuple):
    stack: list[str]


class Valid(NamedTuple):
    line: str


def analyze(line: str) -> Corrupted | Incomplete | Valid:
    stack: list[str] = []
    for c in line:
        if is_opening(c):
            stack.append(c)
        else:
            if not stack:
                return Corrupted(expected=None, got=c)
            if (expect := closing_by_opening[stack.pop()]) != c:
                return Corrupted(expected=expect, got=c)
    if stack:
        return Incomplete(stack)
    return Valid(line)


example_input = """\
[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]
""".splitlines()
my_input = open("input.txt").read().splitlines()


part1_points_by_delim = {")": 3, "]": 57, "}": 1197, ">": 25137}


def part1(lines: list[str]) -> int:
    return sum(
        part1_points_by_delim[c.got]
        for line in lines
        if isinstance((c := analyze(line)), Corrupted)
    )


print(part1(example_input), 26397)
print(part1(my_input), 399153)


def complete(i: Incomplete) -> str:
    s = ''
    while i.stack:
        s += closing_by_opening[i.stack.pop()]
    return s


part2_points_by_delim = {")": 1, "]": 2, "}": 3, ">": 4}


def part2(lines: list[str]) -> int:
    completions = [
        complete(i)
        for line in lines
        if isinstance((i:=analyze(line)), Incomplete)
    ]
    scores: list[int] = []
    for completion in completions:
        score = 0
        for char in completion:
            score *= 5
            score += part2_points_by_delim[char]
        scores.append(score)
    return sorted(scores)[len(scores) // 2]


print(part2(example_input), 288957)
print(part2(my_input), 2995077699)
