"""Advent of code: https://adventofcode.com/2021/day/7
Day 7 Puzzle 2
A giant whale has decided your submarine is its next meal.
Suddenly, a swarm of crabs (each in its own tiny submarine) zooms in to rescue you.
They seem to be preparing to blast a hole in the ocean floor.
The crab submarines all need to be aligned before they'll have enough power to blast
a large enough hole for your submarine to get through.
There's one major catch - crab submarines can only move horizontally.
You quickly make a list of the horizontal position of each crab (your puzzle input).
Crab submarines have limited fuel, so you need to find a way
to make all of their horizontal positions match
while requiring them to spend as little fuel as possible.
For example, consider the following horizontal positions:
16,1,2,0,4,2,7,1,2,14
Crab submarine engines don't burn fuel at a constant rate. Instead, each change of 1 step
in horizontal position costs 1 more unit of fuel than the last: the first step costs 1,
the second step costs 2, the third step costs 3, and so on. As each crab moves,
moving further becomes more expensive.
In this example the best horizontal position to align them all becomes 5:
Move from 16 to 5: 66 fuel
Move from 1 to 5: 10 fuel
Move from 2 to 5: 6 fuel
Move from 0 to 5: 15 fuel
Move from 4 to 5: 1 fuel
Move from 2 to 5: 6 fuel
Move from 7 to 5: 3 fuel
Move from 1 to 5: 10 fuel
Move from 2 to 5: 6 fuel
Move from 14 to 5: 45 fuel
This costs a total of 168 fuel. This is the new cheapest possible outcome.
Determine the horizontal position that the crabs can align to
using the least fuel possible so they can make you an escape route.
How much fuel must they spend to align to that position?
"""

import numpy as np

file_path = 'day_7_data.txt'

# Read the single line containing initial positions.
with open(file_path, 'r') as file_handler:
    start_positions = [int(num) for num in file_handler.readline().split(',')]

start_positions = np.array(start_positions, dtype='int')

# In this puzzle we cannot use median value to identify the optimal alignment position.
# Let's create a lookup list containing fuel expenditure for all possible distances.
min_value = np.min(start_positions)
max_value = np.max(start_positions)

max_distance = max_value - min_value

# Index of each next element in this list will correspond
# to distance and the value (cost) is calculated as the cost
# of getting to the previous step plus n_steps to the current position.
fuel_expenditure = [0]

for i in range(1, max_distance + 1):
    prev_cost = fuel_expenditure[-1]
    fuel_expenditure.append(prev_cost + i)

# We start searching for the optimal alignment point
# from the middle of all start positions and move to outer extreme values
# until estimated fuel expenditure starts getting larger.

mid_position = int(np.round(np.mean(start_positions), 0))
align_point = mid_position

n_values = len(start_positions)

opt_positions = np.array([align_point for _ in range(n_values)], dtype='int')
distances = np.abs(opt_positions - start_positions).reshape((-1, 1))
fuel = np.sum(np.apply_along_axis(lambda x: fuel_expenditure[x[0]], axis=-1, arr=distances))


def estimate_fuel(pos: int) -> int:
    """Function calculates total fuel expenditure
    based on the alignment position.
    :param pos: Alignment position
    :return: Total fuel expenditure
    """
    positions = np.array([pos for _ in range(n_values)], dtype='int')
    distances = np.abs(positions - start_positions).reshape((-1, 1))
    fuel = np.sum(np.apply_along_axis(
        lambda x: fuel_expenditure[x[0]],
        axis=-1,
        arr=distances))
    return fuel


search_downward = True
search_upward = True

for step in range(1, max_distance // 2):
    if not search_upward and not search_downward:
        break
    else:
        if search_downward:
            cur_position = mid_position - step

            if cur_position < 0:
                search_downward = False
                break

            cur_fuel = estimate_fuel(cur_position)
            if cur_fuel < fuel:
                fuel = cur_fuel
                align_point = cur_position
            elif cur_fuel > fuel:
                search_downward = False

        if search_upward:
            cur_position = mid_position + step

            if cur_position > max_value:
                search_upward = False
                break

            cur_fuel = estimate_fuel(cur_position)

            if cur_fuel < fuel:
                fuel = cur_fuel
                align_point = cur_position
            elif cur_fuel > fuel:
                search_upward = False

print(f'At position {align_point} fuel: {fuel}')
