"""Advent of code: https://adventofcode.com/2021/day/2
Day 2 Puzzle 2
You find the submarine manual and discover that in addition to horizontal position and depth,
you also need to track a third value, aim, which also starts at 0. The commands mean something
entirely different than you first thought:
- down X increases your aim by X units
- up X decreases your aim by X units
- forward X does two things:
  - It increases your horizontal position by X units.
  - It increases your depth by your aim multiplied by X.
Using this new interpretation of the commands, calculate the horizontal position and depth
you would have after following the planned course. What do you get if you multiply
your final horizontal position by your final depth?
"""

file_path = 'day_2_data.txt'


class Navigator:
    """Implementation of position monitoring class
    to keep track of submarine movements.
    """
    horizontal_pos = 0
    depth = 0
    aim = 0

    def update_position(self, direction: str, distance: int):
        """Function updates the position of the submarine.
        :param direction: Command to move submarine (one of "forward", "down" or "up")
        :param distance: Distance to move
        :return: None
        """
        if direction == 'forward':
            self.horizontal_pos += distance
            self.depth += distance * self.aim
        elif direction == 'up':
            self.aim -= distance
        else:  # 'down'
            self.aim += distance

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
