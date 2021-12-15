"""Advent of code: https://adventofcode.com/2021/day/7
Day 7 Puzzle 1
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
Each change of 1 step in horizontal position of a single crab costs 1 fuel.
You could choose any horizontal position to align them all on,
but the one that costs the least fuel is horizontal position 2:
Move from 16 to 2: 14 fuel
Move from 1 to 2: 1 fuel
Move from 2 to 2: 0 fuel
Move from 0 to 2: 2 fuel
Move from 4 to 2: 2 fuel
Move from 2 to 2: 0 fuel
Move from 7 to 2: 5 fuel
Move from 1 to 2: 1 fuel
Move from 2 to 2: 0 fuel
Move from 14 to 2: 12 fuel
This costs a total of 37 fuel. This is the cheapest possible outcome;
more expensive outcomes include aligning at position 1 (41 fuel),
position 3 (39 fuel), or position 10 (71 fuel).
Determine the horizontal position that the crabs can align to
using the least fuel possible. How much fuel must they spend to align to that position?
"""

import numpy as np

file_path = 'day_7_data.txt'

# Read the single line containing initial positions.
with open(file_path, 'r') as file_handler:
    start_positions = [int(num) for num in file_handler.readline().split(',')]

# Optimal alignment position for a random set
# of start positions would be the median value.
start_positions = np.array(start_positions)
align_point = np.round(np.median(start_positions), 0)

opt_positions = np.array([align_point for _ in range(len(start_positions))])
fuel = np.sum(np.abs(opt_positions - start_positions))

print(f'At position {align_point} fuel: {fuel}')
