"""Advent of code: https://adventofcode.com/2021/day/11
Day 11 Puzzle 2
You enter a large cavern full of rare bioluminescent dumbo octopuses.
They seem to not like the Christmas lights on your submarine, so you turn them off for now.
There are 100 octopuses arranged neatly in a 10 by 10 grid. Each octopus slowly gains energy
over time and flashes brightly for a moment when its energy is full.
Although your lights are off, maybe you could navigate through the cave
without disturbing the octopuses if you could predict when the flashes of light will happen.
Each octopus has an energy level - your submarine can remotely measure the energy level
of each octopus (your puzzle input). For example:
5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526
The energy level of each octopus is a value between 0 and 9.
Here, the top-left octopus has an energy level of 5,
the bottom-right one has an energy level of 6, and so on.
You can model the energy levels and flashes of light in steps.
During a single step, the following occurs:
- First, the energy level of each octopus increases by 1.
- Then, any octopus with an energy level greater than 9 flashes.
  This increases the energy level of all adjacent octopuses by 1,
  including octopuses that are diagonally adjacent.
  If this causes an octopus to have an energy level greater than 9, it also flashes.
  This process continues as long as new octopuses keep having their energy level
  increased beyond 9. (An octopus can only flash at most once per step.)
- Finally, any octopus that flashed during this step has its energy level set to 0,
  as it used all of its energy to flash.
Adjacent flashes can cause an octopus to flash on a step even if it begins that step with very little energy.
It seems like the individual flashes aren't bright enough to navigate.
However, you might have a better option: the flashes seem to be synchronizing.
In the example above, the first time all octopuses flash simultaneously is step 195.
If you can calculate the exact moments when the octopuses will all flash simultaneously,
you should be able to navigate through the cavern. What is the first step during which all octopuses flash?
"""

import numpy as np

file_path = 'day_11_data.txt'

# Create a 2D array of values.
field = []

with open(file_path, 'r') as file_handler:
    for line in file_handler:
        field.append([int(num) for num in line.strip()])

field = np.array(field)

height = len(field)
width = len(field[0])
n_octopuses = height * width

# Possible steps to adjacent cells.
neighbours = [(0, 1), (0, -1), (1, 0), (-1, 0),
              (1, 1), (-1, -1), (-1, 1), (1, -1)]

# Connectivity graph.
graph = {(i, j): set() for i in range(height) for j in range(width)}

for i in range(height):
    for j in range(width):
        for step_i, step_j in neighbours:
            neigh_i, neigh_j = i + step_i, j + step_j
            if 0 <= neigh_i < height and 0 <= neigh_j < width:
                graph[(i, j)].add((neigh_i, neigh_j))


class FlashCounter:
    """Class for processing and counting flashes per step.
    """
    n_flashes = 0
    n_steps = 0

    def __init__(self, arr, graph):
        self.arr = arr
        self.graph = graph

    def step(self) -> tuple:
        """Function executes 1 step, checking flash conditions
        for all cells and updating neighboring cells until all flashes stop.
        :return: Tuple containing number of flashes in the current step and step ID
        """
        self.arr += 1
        self.n_steps += 1

        # To keep track of flashes for the current step.
        self.cur_flash = self.arr < 0

        found_flashes = self.process_flashes()
        while found_flashes:
            found_flashes = self.process_flashes()

        n_flashes = np.sum(np.sum(self.cur_flash))
        self.n_flashes += n_flashes  # Update counter
        self.arr[np.where(self.cur_flash > 0)] = 0

        return n_flashes, self.n_steps

    def process_flashes(self) -> bool:
        """Function processes one round of flashes.
        :return: Boolean value (if True - flashed cells were found
        and adjacent values updated, if False - no flashes were found)
        """
        mask = np.where(self.arr > 9)
        self.cur_flash[mask] = True
        self.arr[mask] = 0

        n_flashed = len(mask[0])
        if n_flashed > 0:
            self.update_adjacent(mask)  # Increase neighbours
            self.arr[mask] = 0  # Set flashed cells to 0

        return n_flashed > 0

    def update_adjacent(self, mask):
        """Function increases values of adjacent cells.
        :param mask: Coordinates of cells that just flashed
        :return: None
        """
        for idx in zip(mask[0], mask[1]):  # For each cell
            for adj_idx in self.graph[idx]:  # Find all neighbours
                self.arr[adj_idx] += 1

    def result(self):
        print(self.n_flashes)


counter = FlashCounter(field, graph)

while True:
    n_flashes, step = counter.step()
    if n_flashes == n_octopuses:
        print(step)
        break
