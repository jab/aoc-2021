#!/usr/bin/env python3

from collections import Counter
from functools import cache


def parse_input(s: str) -> list[int]:
    return [int(i) for i in s.split(",")]


example_input = parse_input("3,4,3,1,2")
my_input = parse_input(open("input.txt").read())


def solution_recursive(initial: list[int], days: int):
    return sum(count_fish_and_descendants(fish, days) for fish in initial)


@cache
def count_fish_and_descendants(fish: int, days: int) -> int:
    if days == 0:
        return 1
    if fish == 0:
        return (
            count_fish_and_descendants(6, days - 1) +  # this fish, plus...
            count_fish_and_descendants(8, days - 1)    # its newly-spawned descendant
        )
    return count_fish_and_descendants(fish - 1, days - 1)


def solution_nonrecursive(initial: list[int], days: int) -> int:
    freq_by_age = Counter(initial)
    for _ in range(days):
        freq_by_age = {k - 1: v for (k, v) in freq_by_age.items()}
        freq_by_age[8] = freq_by_age.pop(-1, 0)
        freq_by_age[6] = freq_by_age.get(6, 0) + freq_by_age[8]
    return sum(freq_by_age.values())


print(solution_recursive(example_input, 80), 5934)
print(solution_recursive(my_input, 80), 374927)
print(solution_nonrecursive(example_input, 80), 5934)
print(solution_nonrecursive(my_input, 80), 374927)

print(solution_recursive(example_input, 256), 26984457539)
print(solution_recursive(my_input, 256), 1687617803407)
print(solution_nonrecursive(example_input, 256), 26984457539)
print(solution_nonrecursive(my_input, 256), 1687617803407)
