# На шахматной доске стоят белый король и черный конь.
# Конь неподвижен, король может ходить на одну клетку вправо,
# на одну клетку вверх или наискосок вправо-вверх.
# Посчитайте, сколькими способами король может дойти до клетки h8,
# начав с клетки a1. Королю нельзя попадать под атаку коня.
# Самого коня есть тоже нельзя.
# Строки шахматной доски пронумерованы числами от 1 до 8,
# столбцы буквами от a до h.
# Строка 1 - самая нижняя, столбец a - самый левый.
# Формат входных данных
# В единственной строке - позиция коня.
# Позиция - это два символа, буква столбца и номер строки, например a3.
# Формат выходных данных: одно число — результат.

field = [["*" for _ in range(9)] for _ in range(9)]  # Создаем двумерный массив 9 х 9 клеток.
# Заполняем его произвольными символами.

# Нижний ряд и крайний левый столбец не входят в игровое поле.
# Они созданы для удобства вычислений и заполняются нулями.
for i in range(9):
    field[8][i] = 0
    field[i][0] = 0

pos = input()
knight_row = 8 - int(pos[1])  # Вычленяем из шахматной нотации координаты ряда от 0 до 7 в обратном порядке.
knight_column = 'abcdefgh'.find(pos[0]) + 1  # Вычленяем из шахматной нотации координаты столбца от 0 до 7.

field[knight_row][knight_column] = 0  # Обозначаем на поле координаты коня. На эту клетку ходить нельзя.

# Список содержит все возможные варианты ходов коня.
knight_moves = [(-2, -1), (-1, -2), (-2, 1), (-1, 2), (2, -1), (1, -2), (2, 1), (1, 2)]

for element in knight_moves:  # Перебираем все возможные коды коня.
    move_x, move_y = element
    possible_x = knight_row + move_x  # Для каждого случая вычисляем ударные клетки.
    possible_y = knight_column + move_y
    if 0 <= possible_x <= 7 and 1 <= possible_y <= 8:  # Если ударная клетка не выходит за пределы поля,
        field[possible_x][possible_y] = 0  # обозначаем ее в массиве как 0.

if field[7][1]:  # Проверяем, что начальная точка не занята конем и не попадает под удар.
    field[7][1] = 1  # Присваиваем ей значение 1 (способ попасть).

for row in range(7, -1, -1):  # Перебираем массив в границах фактического поля,
    # начиная с последней строки.
    for column in range(1, 9, 1):
        if field[row][column] == 1 or field[row][column] == 0:
            # Если в клетке стоит 0 или 1, переходим на следующий цикл.
            continue
        else:
            field[row][column] = field[row+1][column] + field[row][column-1] + field[row+1][column-1]

print(field[0][8])  # Выводим количество способов попасть в конечную точку.
