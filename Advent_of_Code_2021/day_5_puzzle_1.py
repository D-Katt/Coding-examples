"""Advent of code: https://adventofcode.com/2021/day/5
Day 5 Puzzle 1
You come across a field of hydrothermal vents on the ocean floor.
These vents constantly produce large, opaque clouds.
They tend to form in lines. For example:
0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
Each line of vents is given as a line segment in the format x1,y1 -> x2,y2
where x1,y1 are the coordinates of one end the line segment
and x2,y2 are the coordinates of the other end.
These line segments include the points at both ends. In other words:
An entry like 1,1 -> 1,3 covers points 1,1, 1,2, and 1,3.
An entry like 9,7 -> 7,7 covers points 9,7, 8,7, and 7,7.
For now, only consider horizontal and vertical lines: lines where either x1 = x2 or y1 = y2.
So, the horizontal and vertical lines from the above list would produce the following diagram:
.......1..
..1....1..
..1....1..
.......1..
.112111211
..........
..........
..........
..........
222111....
In this diagram, the top left corner is 0,0 and the bottom right corner is 9,9.
Each position is shown as the number of lines which cover that point
or . if no line covers that point. The top-left pair of 1s, for example, comes from 2,2 -> 2,1;
the very bottom row is formed by the overlapping lines 0,9 -> 5,9 and 0,9 -> 2,9.
To avoid the most dangerous areas, you need to determine the number of points
where at least two lines overlap. In the above example, this is anywhere
in the diagram with a 2 or larger - a total of 5 points.
Consider only horizontal and vertical lines. At how many points do at least two lines overlap?
"""

import numpy as np

file_path = 'day_5_data.txt'

# Create a square field.
field = np.zeros((1000, 1000))

# Read coordinates one by one.
with open(file_path, 'r') as file_handler:
    for line in file_handler:
        coord_1, coord_2 = line.split(' -> ')

        x1, y1 = [int(num) for num in coord_1.split(',')]
        x2, y2 = [int(num) for num in coord_2.split(',')]

        min_x = min(x1, x2)
        max_x = max(x1, x2)
        min_y = min(y1, y2)
        max_y = max(y1, y2)

        # Mark vertical and horizontal lines.
        if min_x == max_x:
            field[min_x, min_y:max_y+1] += 1
        elif min_y == max_y:
            field[min_x:max_x+1, min_y] += 1

# Count cells where more than 1 line was drawn.
print(sum(sum(field > 1)))
