#!/usr/bin/env python3

from functools import reduce
from heapq import nlargest
from operator import mul


Grid = list[list[int]]
Coord = tuple[int, int]


def parse_input(s: str) -> Grid:
    return [[int(i) for i in row] for row in s.splitlines()]


example_input = parse_input("""\
2199943210
3987894921
9856789892
8767896789
9899965678""")

my_input = parse_input(open("input.txt").read())


def neighbors(input: Grid, r: int, c: int) -> list[Coord]:
    nrows = len(input)
    ncols = len(input[0])
    return [
        (r + dr, c + dc)
        for (dr, dc) in ((-1, 0), (1, 0), (0, 1), (0, -1))
        if 0 <= (r + dr) < nrows and 0 <= (c + dc) < ncols
    ]


def is_low(input: Grid, r: int, c: int) -> bool:
    return all(input[r][c] < input[nr][nc] for (nr, nc) in neighbors(input, r, c))


def lows(input: Grid) -> list[Coord]:
    return [
        (r, c)
        for (r, row) in enumerate(input)
        for c in range(len(row))
        if is_low(input, r, c)
    ]


def part1(input: Grid) -> int:
    return sum(input[r][c] + 1 for (r, c) in lows(input))


print(part1(example_input), 15)
print(part1(my_input), 444)


Basin = set[Coord]


def basins(input: Grid) -> list[Basin]:
    bs: list[Basin] = []
    for (r, c) in lows(input):
        visited: set[Coord] = set()
        basin = {(r, c)}
        frontier = {(r, c)}
        while frontier:
            pos = frontier.pop()
            fr, fc = pos
            fval = input[fr][fc]
            visited.add(pos)
            for (nr, nc) in neighbors(input, *pos):
                nval = input[nr][nc]
                if (
                    (nr, nc) not in visited
                    and nval != 9
                    and nval > fval
                ):
                    basin.add((nr, nc))
                    frontier.add((nr, nc))
        bs.append(basin)
    return bs


def part2(input: Grid) -> int:
    top3 = nlargest(3, (len(b) for b in basins(input)))
    return reduce(mul, top3)


print(part2(example_input), 1134)
print(part2(my_input), 1168440)
