"""Advent of code: https://adventofcode.com/2021/day/2
Day 2 Puzzle 1
The submarine can take a series of commands:
- forward X increases the horizontal position by X units
- down X increases the depth by X units
- up X decreases the depth by X units
The submarine follows the course defined in the input file.
Your horizontal position and depth both start at 0.
Calculate the horizontal position and depth you would have after following the planned course.
What do you get if you multiply your final horizontal position by your final depth?
"""

file_path = 'day_2_data.txt'


class Navigator:
    """Implementation of position monitoring class
    to keep track of submarine movements.
    """
    horizontal_pos = 0
    depth = 0

    def update_position(self, direction: str, distance: int):
        """Function updates the position of the submarine.
        :param direction: Command to move submarine (one of "forward", "down" or "up")
        :param distance: Distance to move
        :return: None
        """
        if direction == 'forward':
            self.horizontal_pos += distance
        elif direction == 'up':
            self.depth -= distance
        else:  # 'down'
            self.depth += distance

    def result(self):
        """Function multiplies current depth by horizontal position
        and displays the result.
        :return: None
        """
        print(self.horizontal_pos * self.depth)


analyser = Navigator()

with open(file_path, 'r') as file_handler:
    for line in file_handler:
        direction, distance = line.split()
        distance = int(distance)
        analyser.update_position(direction, distance)

analyser.result()
