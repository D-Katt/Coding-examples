# Valid Sudoku. Determine if a 9x9 Sudoku board is valid.
# Only the filled cells need to be validated according to the following rules:
# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# The Sudoku board could be partially filled,
# where empty cells are filled with the character '.'.
# Example 1:
# Input:
# 5,3,.,.,7,.,.,.,.
# 6,.,.,1,9,5,.,.,.
# .,9,8,.,.,.,.,6,.
# 8,.,.,.,6,.,.,.,3
# 4,.,.,8,.,3,.,.,1
# 7,.,.,.,2,.,.,.,6
# .,6,.,.,.,.,2,8,.
# .,.,.,4,1,9,.,.,5
# .,.,.,.,8,.,.,7,9
# Output: true
# Example 2:
# Input:
# 8,3,.,.,7,.,.,.,.
# 6,.,.,1,9,5,.,.,.
# .,9,8,.,.,.,.,6,.
# 8,.,.,.,6,.,.,.,3
# 4,.,.,8,.,3,.,.,1
# 7,.,.,.,2,.,.,.,6
# .,6,.,.,.,.,2,8,.
# .,.,.,4,1,9,.,.,5
# .,.,.,.,8,.,.,7,9
# Output: false
# Explanation: Same as Example 1, except with the 5 in the top left corner being
# modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
# Note:
# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.
# The given board contain only digits 1-9 and the character '.'.
# The given board size is always 9x9.

# Формируем двумерную матрицу для судоку размером 9 х 9:
sudoku = [None] * 9

# Считываем значения строк (разделителем служит запятая)
# и добавляем их в матрицу:
for i in range(9):
    sudoku[i] = [s for s in input().split(',')]

# Проверяем строки матрицы в поисках дублирующихся чисел.
for i in range(9):
    elements = set()  # Создаем множество для проверки дублей.
    for el in sudoku[i]:  # В каждой строке последовательно перебираем элементы.
        if el != '.':  # Если очередной элемент не является точкой,
            if el in elements:  # проверяем, встречался ли он раньше.
                print('false')
                exit()
            else:
                elements.add(el)

# Проверяем столбцы матрицы в поисках дублирующихся чисел.
for j in range(9):
    elements = set()  # Создаем множество для проверки дублей.
    for i in range(9):  # В каждом столбце последовательно перебираем элементы.
        if sudoku[i][j] != '.':  # Если очередной элемент не является точкой,
            if sudoku[i][j] in elements:  # проверяем, встречался ли он раньше.
                print('false')
                exit()
            else:
                elements.add(sudoku[i][j])

# Проверяем квадраты 3 х 3 внутри матрицы в поисках дублирующихся чисел.
for row_step in (0, 3, 6):
    for column_step in (0, 3, 6):
        elements = set()  # Создаем множество для проверки дублей.
        for i in range(3):
            for j in range(3):  # Перебираем квадраты 3 х 3 клетки.
                row_pos = row_step + i  # Прибавляем шаг к текущему значению i и j.
                column_pos = column_step + j
                if sudoku[row_pos][column_pos] != '.':  # Если очередной элемент не является точкой,
                    if sudoku[row_pos][column_pos] in elements:  # проверяем, встречался ли он раньше.
                        print('false')
                        exit()
                    else:
                        elements.add(sudoku[row_pos][column_pos])

# Если предыдущие проверки не выявили дублирующихся чисел,
# таблица судоку является правильной.
print('true')
