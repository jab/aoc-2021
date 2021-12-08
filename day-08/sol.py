from collections import Counter, defaultdict

digit_by_nsegments = {
    2: 1,
    4: 4,
    3: 7,
    7: 8,
}

example_input = """\
be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce
"""
my_input = open("input.txt").read()

def part1(s: str):
    words = [word for line in s.splitlines() for word in line.split(' | ', maxsplit=1)[-1].split()]
    return sum(1 for w in words if len(w) in digit_by_nsegments)

print(part1(example_input), 26)
print(part1(my_input), 352)


segments_by_digit = {
    '0': 'abcefg',
    '1': 'cf',
    '2': 'acdeg',
    '3': 'acdfg',
    '4': 'bcdf',
    '5': 'abdfg',
    '6': 'abdefg',
    '7': 'acf',
    '8': 'abcdefg'
}

def part2(s):
    lines = s.splitlines()
    for line in lines:
        candidates_by_sample = defaultdict(set)
        samples, _, results = line.partition(' | ')
        samples = [sorted(i) for i in samples.split()]
        results = [sorted(i) for i in results.split()]
        for sample in samples:
            candidates_by_sample[sample]


