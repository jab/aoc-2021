from functools import partial
import typing

example_input = [int(i) for i in "16,1,2,0,4,2,7,1,2,14".split(",")]
my_input = [int(i) for i in open("input.txt").read().split(",")]


def cost1(current: int, target: int) -> int:
    return abs(target - current)


def cost2(current: int, target: int) -> int:
    delta = abs(target - current)
    return delta * (delta + 1) // 2


def minfuel(xs: list[int], costfn: typing.Callable[[int, int], int]) -> int:
    best = float('inf')
    for t in range(min(xs), max(xs) + 1):
        cost = sum(costfn(x, t) for x in xs)
        if cost < best:
            best = cost
    return typing.cast(int, best)


part1: typing.Callable[[list[int]], int] = partial(minfuel, costfn=cost1)
part2: typing.Callable[[list[int]], int] = partial(minfuel, costfn=cost2)

print(part1(example_input), 37)
print(part1(my_input), 344535)

print(part2(example_input), 168)
print(part2(my_input), 95581659)
