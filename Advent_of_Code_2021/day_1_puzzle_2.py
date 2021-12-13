"""Advent of code: https://adventofcode.com/2021/day/1
Day 1 Puzzle 2
As the submarine drops below the surface of the ocean, it automatically performs a sonar sweep
of the nearby sea floor. Every single measurement isn't very useful: there's too much noise in the data.
Instead, consider sums of a three-measurement sliding window and count the number of times
the sum of measurements in this sliding window increases from the previous sum.
"""

file_path = 'day_1_data.txt'


class SlidingWindow:
    """Implementation of stack-like data structure (FIFO)
    to keep track of the last three measurements
    and dynamically update and compare sums of values
    in the current and previous triplet.
    """
    prev_values = []  # To dynamically update previous measurements.
    counter = 0

    def add_value(self, value: int):
        """Function adds a new measurement to the stack,
        compares current tree measurements with the previous measurements
        and updates the counter of increases.
        :param value: New value
        :return: None
        """
        if len(self.prev_values) == 3:
            prev_sum = sum(self.prev_values)
            del self.prev_values[0]

            if value + sum(self.prev_values) > prev_sum:
                self.counter += 1

        self.prev_values.append(value)

    def result(self):
        """Function displays the number of increases in 3-value sums
        of measurements sequence.
        :return: None
        """
        print(self.counter)


analyser = SlidingWindow()

with open(file_path, 'r') as file_handler:
    for line in file_handler:
        cur_measure = int(line)
        analyser.add_value(cur_measure)

analyser.result()
