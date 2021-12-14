"""Advent of code: https://adventofcode.com/2021/day/4
Day 4 Puzzle 2
Bingo is played on a set of boards each consisting of a 5x5 grid of numbers.
Numbers are chosen at random, and the chosen number is marked on all boards
on which it appears. (Numbers may not appear on all boards.) If all numbers
in any row or any column of a board are marked, that board wins. (Diagonals don't count.)
The first row of the input file contains randomly drawn numbers.
The next rows contain 5x5 grids of numbers separated by new line.
For example:
7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7

Keep track of the drawn numbers and mark them on all boards.
Find the board that will win last and calculate the win score
for this board: find the sum of all unmarked numbers on that board
and multiply that sum by the number that was just called when the board won.
"""

import numpy as np

file_path = 'day_4_data.txt'

# Read all contents of the file as a list of strings.
with open(file_path, 'r') as file_handler:
    data = file_handler.readlines()

# Extract sequence of random numbers from the first row.
numbers = [int(num) for num in data[0].strip().split(',')]

# Stack all boards vertically.
all_boards = []

for row in data[2:]:
    if len(row) != 1:  # Skip empty lines.
        all_boards.append([int(num) for num in row.strip().split()])

all_boards = np.array(all_boards, dtype='float')

n_boards = len(all_boards) // 5  # Total number of boards.
winning_boards = [False] * n_boards

# Delete numbers one by one from all boards.
end_game = False

for num in numbers:
    mask = np.where(all_boards == num)
    all_boards[mask] = np.nan

    # Check if any board has empty row or column.
    for idx, board in enumerate(np.split(all_boards, n_boards)):
        marked_nums = np.isnan(board)
        rows = np.sum(marked_nums, axis=1)
        columns = np.sum(marked_nums, axis=0)

        if np.any(rows == 5) or np.any(columns == 5):
            winning_boards[idx] = True  # Update board state.

            if sum(winning_boards) == n_boards:  # The last winning board.
                end_game = True
                break

    if end_game:
        break

# Multiply the sum of all numbers of the winning board
# by the last drawn number.
mask = np.where(np.isnan(board))
win_board = board.copy()
win_board[mask] = 0

score = num * sum(sum(win_board))
print(score)
