"""Advent of code: https://adventofcode.com/2021/day/1
Day 1 Puzzle 1
As the submarine drops below the surface of the ocean, it automatically performs a sonar sweep
of the nearby sea floor. Count the number of times a depth measurement increases
from the previous measurement. (There is no measurement before the first measurement.)
In the example below there are 7 measurements that are larger than the previous measurement:
199 (N/A - no previous measurement)
200 (increased)
208 (increased)
210 (increased)
200 (decreased)
207 (increased)
240 (increased)
269 (increased)
260 (decreased)
263 (increased)
"""

file_path = 'day_1_data.txt'

increase_count = 0
prev = -1  # All measurements are positive.

with open(file_path, 'r') as file_handler:
    for line in file_handler:
        cur_measure = int(line)
        if cur_measure > prev:
            increase_count += 1
        prev = cur_measure

# Subtract 1 for the first measurement in sequence.
increase_count -= 1
print(increase_count)
