"""Advent of code: https://adventofcode.com/2021/day/8
Day 8 Puzzle 2
Input file contains entries of the submarine systems. Each entry consists
of ten unique signal patterns, a | delimiter, and finally the four digit output value.
Example of an entry:
acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf
The unique signal patterns would correspond to the following digits:
acedgfb: 8
cdfbe: 5
gcdfa: 2
fbcad: 3
dab: 7
cefabd: 9
cdfgeb: 6
eafb: 4
cagedb: 0
ab: 1
But connections are mismatched and actual letters could be present in random order.
Within an entry, the same wire/segment connections are used (but you don't know
what the connections actually are). The unique signal patterns correspond to the ten
different ways the submarine tries to render a digit using the current wire/segment connections.
To render a 1, only two different segments would be turned on; the rest would be off.
To render a 7, only three different segments would be turned on.
To render a 4, four different segments would be turned on.
To render an 8, seven different segments would be turned on.
Some digits have equal number of characters but in different combinations.
To render 2, 3 or 5, five different segments would be turned on.
To render 0, 6 or 9, six different segments would be turned on.

Using this information all output values in the entries below could be deduced:
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
Corresponding output values:
fdgacbe cefdb cefbgd gcbe: 8394
fcgedb cgb dgebacf gc: 9781
cg cg fdcagb cbg: 1197
efabcd cedba gadfec cb: 9361
gecf egdcabf bgf bfgea: 4873
gebdcfa ecba ca fadegcb: 8418
cefg dcbef fcge gbcadfe: 4548
ed bcgafe cdgba cbgef: 1625
gbdfcae bgc cg cgb: 8717
fgae cfgab fg bagce: 4315
Adding all of the output values in this example produces 61229.
For each entry, determine all of the wire/segment connections and decode the four-digit output values.
What do you get if you add up all of the output values?
"""

from itertools import permutations

file_path = 'day_8_data.txt'

# This "brute-force" solution takes a while to complete.

# Link digits to the original combinations of letters.
letters_to_digits_unsorted = {
    'acedgfb': '8', 'cdfbe': '5', 'gcdfa': '2', 'fbcad': '3', 'dab': '7',
    'cefabd': '9', 'cdfgeb': '6', 'eafb': '4', 'cagedb': '0', 'ab': '1'
}

# Create a dictionary with sorted letter-keys.
letters_to_digits = dict()
for key, value in letters_to_digits_unsorted.items():
    letters_to_digits[''.join(sorted(key))] = value

total = 0

# Read entries one by one.
with open(file_path, 'r') as file_handler:
    for line in file_handler:
        display_vals, output_vals = line.strip().split(' | ')

        display_vals = display_vals.split()
        output_vals = output_vals.split()

        # For each random shift of original letters
        for permutation in permutations('abcdefg'):
            # create a dictionary where each original character
            # is mapped to a character in permuted string.
            trans_dict = str.maketrans('abcdefg', ''.join(permutation))
            # Replace characters in left and right parts of the entry.
            perm_display_vals = [''.join(sorted(code.translate(trans_dict))) for code in display_vals]
            perm_output_vals = [''.join(sorted(code.translate(trans_dict))) for code in output_vals]
            # If all letter combinations in the left part are valid digits,
            # stop the search and add 4-digit value from the right part.
            if all(combination in letters_to_digits for combination in perm_display_vals):
                total += int(''.join(letters_to_digits[char] for char in perm_output_vals))
                break

print(total)
