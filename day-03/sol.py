#!/usr/bin/env python3

import itertools
import typing as t
from types import SimpleNamespace


def part1_power_consumption(diagnostic_report: t.Sequence[str]) -> int:
    min2win = len(diagnostic_report) // 2  # beat this number to win popcount
    bit_len = len(diagnostic_report[0])
    parities = [0] * bit_len
    for s in diagnostic_report:
        for i, c in enumerate(s):
            if abs(parities[i]) <= min2win:
                parities[i] += 1 if c == '1' else - 1  # (c == '1')*2-1 is too clever ;)
    gamma = ''
    epsilon = ''
    for p in parities:
        assert p != 0, "No spec for how to handle ties"
        gamma += str(0 + (p > 0))
        epsilon += str(0 + (p < 0))
    gamma = int(gamma, base=2)
    epsilon = int(epsilon, base=2)
    return gamma * epsilon


def part2_life_support_rating(diagnostic_report: t.Sequence[str]) -> int:
    nreadings = len(diagnostic_report)
    bit_len = len(diagnostic_report[0])
    candidates_initial = set(diagnostic_report)
    o2ns = SimpleNamespace(
        candidates=candidates_initial,
        winner=lambda x: '0' if x < 0 else '1',
    )
    co2ns = SimpleNamespace(
        candidates=candidates_initial.copy(),
        winner=lambda x: '1' if x < 0 else '0',
    )
    for (i, ns) in itertools.product(range(bit_len), (o2ns, co2ns)):
        if len(ns.candidates) == 1:
            continue
        min2win = len(ns.candidates) // 2  # beat this number to win popcount
        parity = 0
        for c in ns.candidates:
            parity += 1 if c[i] == '1' else -1
            if abs(parity) > min2win:
                break
        winner = ns.winner(parity)
        ns.candidates -= {c for c in ns.candidates if c[i] != winner}
    o2_rating = int(next(iter(o2ns.candidates)), base=2)
    co2_rating = int(next(iter(co2ns.candidates)), base=2)
    return o2_rating * co2_rating


example_input = "00100 11110 10110 10111 10101 01111 00111 11100 10000 11001 00010 01010".split()
my_input = open("input.txt").read().split()
print(part1_power_consumption(example_input), 198)
print(part1_power_consumption(my_input), 2954600)
print(part2_life_support_rating(example_input), 230)
print(part2_life_support_rating(my_input), 1662846)
