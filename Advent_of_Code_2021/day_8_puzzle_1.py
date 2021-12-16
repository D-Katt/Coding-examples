"""Advent of code: https://adventofcode.com/2021/day/8
Day 8 Puzzle 1
Input file contains entries of the submarine systems. Each entry consists
of ten unique signal patterns, a | delimiter, and finally the four digit output value.
Example of an entry:
acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf
Within an entry, the same wire/segment connections are used (but you don't know
what the connections actually are). The unique signal patterns correspond to the ten
different ways the submarine tries to render a digit using the current wire/segment connections.
To render a 1, only two different segments would be turned on; the rest would be off.
To render a 7, only three different segments would be turned on.
To render a 4, four different segments would be turned on.
To render an 8, seven different segments would be turned on.
The entries below have 26 instances of these 4 digits (1, 4, 7 and 8) in the output values:
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
Highlighted values (by entries):
fdgacbe gcbe
cgb dgebacf gc
cg cg cbg
cb
gecf egdcabf bgf
gebdcfa ecba ca fadegcb
cefg fcge gbdfcae
ed
gbdfcae bgc cg cgb
fgae fg
In the output values of the input file, how many times do digits 1, 4, 7, or 8 appear?
"""

file_path = 'day_8_data.txt'

total = 0

# Read entries one by one.
with open(file_path, 'r') as file_handler:
    for line in file_handler:
        _, output_vals = line.strip().split(' | ')
        output_vals = output_vals.split()

        # Count number of output values with 2, 3, 4 or 7 distinct letters.
        for combination in output_vals:
            if len(combination) in {2, 3, 4, 7}:
                total += 1

print(total)
