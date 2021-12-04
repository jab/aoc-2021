#!/usr/bin/env python3

# https://adventofcode.com/2021/day/1

import itertools
import typing as t


def part1_num_pairwise_increases(ints: t.Iterable[int]) -> int:
    return sum(j > i for (i, j) in itertools.pairwise(ints))


def part2_num_increasing_triple_sums(ints: t.Iterable[int]) -> int:
    # We ultimately only care about pairwise comparisons of consecutive
    # triples' sums, so we don't have to bother adding the common elements of
    # the consecutive triples, since they just get canceled out anyway:
    #   (x1 + x2 + x3) > (x0 + x1 + x2)
    #   (x1 + x2 + x3) - (x0 + x1 + x2) > 0
    #              x3  -  x0            > 0
    # Note also that this generalizes for any window size, e.g. 4:
    #   (x1 + x2 + x3 + x4) - (x0 + x1 + x2 + x3) == x4 - x0
    a, b = itertools.tee(ints)
    next(itertools.islice(b, 3, 3), None)  # drop first 3 elements of b
    return sum(j > i for (i, j) in zip(a, b))


example_input = [int(i) for i in "199 200 208 210 200 207 240 269 260 263".split()]
print(part1_num_pairwise_increases(example_input), 7)
print(part2_num_increasing_triple_sums(example_input), 5)

my_input = [int(i.strip()) for i in open("input.txt")]
print(part1_num_pairwise_increases(my_input), 1266)
print(part2_num_increasing_triple_sums(my_input), 1217)


################################################################################
# For funsies, here is a generalization of itertools.pairwise, triplewise, etc.:
T = t.TypeVar("T")

def nwise(n: int, it: t.Iterable[T]) -> t.Iterable[t.Tuple[T, ...]]:
    """
    Length *n* sliding window over *it*.

    >>> seq = (0, 1, 2, 3)
    >>> list(nwise(1, seq))
    [(0,), (1,), (2,), (3,)]
    >>> list(nwise(2, seq))
    [(0, 1), (1, 2), (2, 3)]
    >>> list(nwise(3, seq))
    [(0, 1, 2), (1, 2, 3)]
    >>> list(nwise(4, seq))
    [(0, 1, 2, 3)]
    """
    it = iter(it)
    win = collections.deque(itertools.islice(it, n), maxlen=n)
    if len(win) == n:
        yield tuple(win)
    for i in it:
        win.append(i)
        yield tuple(win)


# pairwise = functools.partial(nwise, 2)
# triplewise = functools.partial(nwise, 3)
