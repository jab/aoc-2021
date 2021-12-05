#!/usr/bin/env python3

from collections import defaultdict
from itertools import repeat
from functools import partial
import re


def parse_and_sum_overlapping(s: str, diag=False) -> int:
    board = defaultdict(lambda: defaultdict(int))
    for line in s.splitlines():
        x1, y1, x2, y2 = (int(i) for i in re.split("\D", line) if i)
        if not diag and not (x1 == x2 or y1 == y2):
            continue
        dx = (x2 > x1) - (x2 < x1)
        dy = (y2 > y1) - (y2 < y1)
        xs = range(x1, x2 + dx, dx) if dx else repeat(x1)
        ys = range(y1, y2 + dy, dy) if dy else repeat(y1)
        for x, y in zip(xs, ys):
            board[x][y] += 1
    return sum(i > 1 for col in board.values() for i in col.values())


part1 = partial(parse_and_sum_overlapping, diag=False)
part2 = partial(parse_and_sum_overlapping, diag=True)


example_input = """\
0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
"""
my_input = open("input.txt").read()

print(part1(example_input), 5)
print(part1(my_input), 7318)

print(part2(example_input), 12)
print(part2(my_input), 19939)
