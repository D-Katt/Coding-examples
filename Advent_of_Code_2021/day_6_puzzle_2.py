"""Advent of code: https://adventofcode.com/2021/day/6
Day 6 Puzzle 2
You should model growth rate for lanternfish. Each lanternfish creates a new lanternfish once every 7 days.
However, this process isn't necessarily synchronized between every lanternfish -
one lanternfish might have 2 days left until it creates another lanternfish,
while another might have 4. So, you can model each fish as a single number
that represents the number of days until it creates a new lanternfish.
A new lanternfish needs slightly longer before it's capable of producing
more lanternfish: two more days for its first cycle.
So, suppose you have a lanternfish with an internal timer value of 3:
- After one day, its internal timer would become 2.
- After another day, its internal timer would become 1.
- After another day, its internal timer would become 0.
- After another day, its internal timer would reset to 6,
  and it would create a new lanternfish with an internal timer of 8.
- After another day, the first lanternfish would have an internal timer of 5,
  and the second lanternfish would have an internal timer of 7.
A lanternfish that creates a new fish resets its timer to 6, not 7
(because 0 is included as a valid timer value). The new lanternfish starts
with an internal timer of 8 and does not start counting down until the next day.
The submarine automatically produces a list of the ages of several hundred nearby lanternfish
(your puzzle input). For example, suppose you were given the following list:
3,4,3,1,2
This list means that the first fish has an internal timer of 3,
the second fish has an internal timer of 4, and so on until the fifth fish,
which has an internal timer of 2.
Simulating these fish over several days would proceed as follows:
Initial state: 3,4,3,1,2
After  1 day:  2,3,2,0,1
After  2 days: 1,2,1,6,0,8
After  3 days: 0,1,0,5,6,7,8
After  4 days: 6,0,6,4,5,6,7,8,8
After  5 days: 5,6,5,3,4,5,6,7,7,8
After  6 days: 4,5,4,2,3,4,5,6,6,7
After  7 days: 3,4,3,1,2,3,4,5,5,6
After  8 days: 2,3,2,0,1,2,3,4,4,5
After  9 days: 1,2,1,6,0,1,2,3,3,4,8
After 10 days: 0,1,0,5,6,0,1,2,2,3,7,8
After 11 days: 6,0,6,4,5,6,0,1,1,2,6,7,8,8,8
After 12 days: 5,6,5,3,4,5,6,0,0,1,5,6,7,7,7,8,8
After 13 days: 4,5,4,2,3,4,5,6,6,0,4,5,6,6,6,7,7,8,8
After 14 days: 3,4,3,1,2,3,4,5,5,6,3,4,5,5,5,6,6,7,7,8
After 15 days: 2,3,2,0,1,2,3,4,4,5,2,3,4,4,4,5,5,6,6,7
After 16 days: 1,2,1,6,0,1,2,3,3,4,1,2,3,3,3,4,4,5,5,6,8
After 17 days: 0,1,0,5,6,0,1,2,2,3,0,1,2,2,2,3,3,4,4,5,7,8
After 18 days: 6,0,6,4,5,6,0,1,1,2,6,0,1,1,1,2,2,3,3,4,6,7,8,8,8,8
Each day, a 0 becomes a 6 and adds a new 8 to the end of the list,
while each other number decreases by 1 if it was present at the start of the day.
In this example, after 18 days, there are a total of 26 fish. After 80 days, there would be a total of 5934.
Suppose the lanternfish live forever and have unlimited food and space.
After 256 days in the example above, there would be a total of 26984457539 lanternfish.
How many lanternfish would there be after 256 days?
"""

from collections import Counter

file_path = 'day_6_data.txt'

# Read the single line containing initial state for all fish.
with open(file_path, 'r') as file_handler:
    fish_list = [int(num) for num in file_handler.readline().split(',')]

# Count the number of fishes at each state.
fish_by_state = Counter(fish_list)
state_list = list(fish_by_state.keys())

# 256 days = 16 * 16 days
# Algorithm to avoid exponentially growing complexity of calculations:
# - Calculate how many fish each state will produce in 16 days and create a lookup dict.
# - Find out initial fish distribution by state.
# - Run through lookup dict 16 times updating total fish distribution.

# Lookup dictionary
growth_dict = dict()

# Find out distribution of fish states that could be produced
# by each individual state in 16 days.
for state in range(9):
    cur_list = [state]

    for i in range(16):  # 16 days
        n_fish = len(cur_list)

        # Change only the values present at the beginning of this iteration.
        for j in range(n_fish):
            if cur_list[j] == 0:
                cur_list[j] = 6
                cur_list.append(8)  # New fish.
            else:
                cur_list[j] -= 1

    growth_dict[state] = Counter(cur_list)

# Run through the lookup dictionary 16 times updating fish_by_state
# after each iteration.
for period in range(16):
    end_period_distr = Counter()

    for state in fish_by_state:
        subset = growth_dict[state].copy()

        for key in subset.keys():
            subset[key] = subset[key] * fish_by_state[state]

        end_period_distr.update(subset)

    fish_by_state = end_period_distr

total = 0  # Total number of fishes after 16 runs.

for val in fish_by_state.values():
    total += val

print(total)
