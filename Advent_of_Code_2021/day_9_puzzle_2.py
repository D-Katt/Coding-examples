"""Advent of code: https://adventofcode.com/2021/day/9
Day 9 Puzzle 2
These caves seem to be lava tubes. Parts are even still volcanically active;
small hydrothermal vents release smoke into the caves that slowly settles like rain.
If you can model how the smoke flows through the caves, you might be able to avoid it
and be that much safer. The submarine generates a heightmap of the floor
of the nearby caves for you (your puzzle input).
Smoke flows to the lowest point of the area it's in.
Low points - the locations that are lower than any of its adjacent locations.
Most locations have four adjacent locations (up, down, left, and right);
locations on the edge or corner of the map have three or two adjacent locations, respectively.
(Diagonal locations do not count as adjacent.)
You need to find the largest basins so you know what areas are most important to avoid.
A basin is all locations that eventually flow downward to a single low point.
Therefore, every low point has a basin, although some basins are very small.
Locations of height 9 do not count as being in any basin, and all other locations
will always be part of exactly one basin.
The size of a basin is the number of locations within the basin, including the low point.
For example, consider the following heightmap:
2199943210
3987894921
9856789892
8767896789
9899965678
The example above has four basins.
The top-left basin, size 3.
The top-right basin, size 9.
The middle basin, size 14.
The bottom-right basin, size 9.
Find the three largest basins and multiply their sizes together.
In the above example, this is 9 * 14 * 9 = 1134.
What do you get if you multiply together the sizes of the three largest basins?
"""

from collections import deque

file_path = 'day_9_data.txt'

# Create a 2D matrix for all values.
with open(file_path, 'r') as file_handler:
    field = file_handler.readlines()
    field = [[int(num) for num in list(line.strip())] for line in field]

height = len(field)
width = len(field[0])

# Possible steps to the neighbours.
neighbours = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# Connectivity graph.
graph = {(i, j): set() for i in range(height) for j in range(width)}

for i in range(height):
    for j in range(width):
        for step_i, step_j in neighbours:
            neigh_i, neigh_j = i + step_i, j + step_j
            if 0 <= neigh_i < height and 0 <= neigh_j < width:
                graph[(i, j)].add((neigh_i, neigh_j))


def define_basin(pos_i: int, pos_j: int) -> int:
    """Function defines the basin size given the low point coordinates.
    :param pos_i: Row index in a 2D matrix
    :param pos_j: Column index in a 2D matrix
    :return: Size of the basin (number of points)
    """
    basin = set()
    basin.add((pos_i, pos_j))

    visited = [[False] * width for _ in range(height)]
    visited[pos_i][pos_j] = True

    queue = deque([(pos_i, pos_j)])
    while queue:
        cur_i, cur_j = queue.popleft()

        for neigh_i, neigh_j in graph[(cur_i, cur_j)]:
            if field[neigh_i][neigh_j] == 9:
                continue
            else:
                if not visited[neigh_i][neigh_j]:
                    visited[neigh_i][neigh_j] = True
                    basin.add((neigh_i, neigh_j))
                    queue.append((neigh_i, neigh_j))

    return len(basin)


basins = []  # List of all basins.

for i in range(height):
    for j in range(width):
        cur_value = field[i][j]
        low_point = True

        for neigh_i, neigh_j in graph[(i, j)]:
            if field[neigh_i][neigh_j] <= cur_value:
                low_point = False
                break

        if low_point:
            basins.append(define_basin(i, j))

basins.sort(reverse=True)
result = basins[0] * basins[1] * basins[2]

print(result)
