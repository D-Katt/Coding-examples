"""Advent of code: https://adventofcode.com/2021/day/3
Day 3 Puzzle 1
The submarine diagnostic report (input file) consists of a list of binary numbers.
The first parameter to check is the power consumption.
You need to use the binary numbers in the diagnostic report to generate two new binary numbers
(called the gamma rate and the epsilon rate). The power consumption can then be found
by multiplying the gamma rate by the epsilon rate.
Each bit in the gamma rate can be determined by finding the most common bit
in the corresponding position of all numbers in the diagnostic report.
For example, given the following diagnostic report:
00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
Considering only the first bit of each number, there are five 0 bits and seven 1 bits.
Since the most common bit is 1, the first bit of the gamma rate is 1.
Following this procedure, the gamma rate is the binary number 10110, or 22 in decimal.
The epsilon rate is calculated in a similar way; rather than use the most common bit,
the least common bit from each position is used. So, the epsilon rate is 01001, or 9 in decimal.
Multiplying the gamma rate (22) by the epsilon rate (9) produces the power consumption, 198.
Use the binary numbers in your diagnostic report to calculate the gamma rate and epsilon rate,
then multiply them together. What is the power consumption of the submarine?
(Be sure to represent your answer in decimal, not binary.)
"""

file_path = 'day_3_data.txt'

# We need to know how many characters each line in the input file contains.
with open(file_path, 'r') as file_handler:
    line = file_handler.readline()
    n_chars = len(line) - 1  # Without end of line symbol

# Index positions in the list correspond to index positions
# of characters in the binary numbers.
counter = [[0, 0] for _ in range(n_chars)]

with open(file_path, 'r') as file_handler:
    for line in file_handler:
        for idx, char in enumerate(line.strip()):
            counter[idx][int(char)] += 1

# Reconstruct gamma and epsilon comparing number of zeroes and ones
# at every index position.
gamma = ''
epsilon = ''

for zeros, ones in counter:
    if zeros > ones:
        gamma = gamma + '0'
        epsilon = epsilon + '1'
    else:
        gamma = gamma + '1'
        epsilon = epsilon + '0'

# Convert to integers and multiply.
gamma = int(gamma, 2)
epsilon = int(epsilon, 2)

mtpl = gamma * epsilon
print(mtpl)
