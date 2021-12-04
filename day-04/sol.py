#!/usr/bin/env python3

import itertools


Draws = list[int]
Board = list[list[int | None]]
Boards = list[Board]


def is_bingo(board: Board) -> bool:
    for rows in (board, zip(*board)):
        if any(all(i is None for i in row) for row in rows):
            return True
    return False


def coords(N: int):
    return itertools.product(range(N), range(N))


def part1(draws: Draws, boards: Boards) -> int:
    N = len(boards[0])
    for (draw, board) in itertools.product(draws, boards):
        for (r, c) in coords(N):
            if board[r][c] == draw:
                board[r][c] = None
        if is_bingo(board):
            return draw * sum(board[r][c] or 0 for (r, c) in coords(N))
    raise AssertionError("Input results in no bingos")


def part2(draws: Draws, boards: Boards) -> int:
    N = len(boards[0])
    pre_bingo = set(id(b) for b in boards)
    for (draw, board) in itertools.product(draws, boards):
        for (r, c) in coords(N):
            if board[r][c] == draw:
                board[r][c] = None
        if is_bingo(board):
            pre_bingo.discard(id(board))
            if not pre_bingo:
                return draw * sum(board[r][c] or 0 for (r, c) in coords(N))
    raise AssertionError("Input results in no bingos")


def parse_input(s: str) -> tuple[Draws, Boards]:
    drawsline, *boards = s.split("\n\n")
    draws = [int(i) for i in drawsline.split(",")]
    boards = [
        [[int(i) for i in line.split()] for line in board.splitlines()]
        for board in boards
    ]
    return draws, boards


example_input = parse_input("""\
7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7""")

my_input = parse_input(open("input.txt").read())

print(part1(*example_input), 4512)
print(part1(*my_input), 12796)

print(part2(*example_input), 1924)
print(part2(*my_input), 18063)
