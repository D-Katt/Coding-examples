# Игрушечный лабиринт представляет собой прозрачную плоскую прямоугольную коробку,
# внутри которой есть препятствия и перемещается шарик. Лабиринт можно наклонять влево,
# вправо, к себе или от себя, после каждого наклона шарик перемещается
# в заданном направлении до ближайшего препятствия или до стенки лабиринта,
# после чего останавливается.
# Целью игры является загнать шарик в одно из специальных отверстий – выходов.
# Шарик проваливается в отверстие, если оно встречается на его пути
# (шарик не обязан останавливаться в отверстии).
# Первоначально шарик находится в левом верхнем углу лабиринта.
# Гарантируется, что решение существует и левый верхний угол
# не занят препятствием или отверстием.
# Формат входных данных
# В первой строке входного файла записаны числа N и M – размеры лабиринта
# (целые положительные числа, не превышающие 100).
# Затем идет N строк по M чисел в каждой – описание лабиринта.
# Число 0 в описании означает свободное место, число 1 – препятствие, число 2 – отверстие.
# Формат выходных данных
# Выведите единственное число – минимальное количество наклонов,
# которые необходимо сделать, чтобы шарик покинул лабиринт через одно из отверстий.

from collections import deque

n, m = (int(s) for s in input().split())

# Описание лабиринта в виде двумерного массива:
labyrinth = [0] * (n + 2)
# Количество строк и столбцов увеличиваем на 2, чтобы обозначить препятствия по периметру лабиринта.

for i in range(1, n + 1):  # Считываем построчно описание лабиринта
    labyrinth[i] = [1] + [int(s) for s in input().split()] + [1]

# Заполняем препятствиями 0-ю и последнюю строку:
labyrinth[0] = labyrinth[n + 1] = [1] * (m + 2)

start = (1, 1)  # Исходная позиция шарика в лабиринте

# Описание посещенных клеток лабиринта в виде словаря
# с указанием расстояния от стартовой клетки:
visited = {start: 0}

queue = deque([start])  # Очередь для перебора ходов в лабиринте

while queue:
    # Пока в очереди есть элементы, берем первый:
    cur_row, cur_column = queue.popleft()

    for i in range(1, m + 2):
        next_row, next_column = cur_row, cur_column + i  # Движение вправо от тек. позиции

        if labyrinth[next_row][next_column] == 2:  # Если встречаем 2, выводим кол-во ходов
            print(visited[(cur_row, cur_column)] + 1)
            exit()

        # Если встречаем 1, проверяем, что предыдущая клетка не была посещена
        # ранее, и добавляем ее в множество посещенных и в очередь.
        elif labyrinth[next_row][next_column] == 1:
            if (next_row, next_column - 1) not in visited:
                visited[(next_row, next_column - 1)] = visited[(cur_row, cur_column)] + 1
                queue.append((next_row, next_column - 1))
                break
            else:  # Если встретили 1, но уже были здесь, прерываем цикл.
                break

    for i in range(1, m + 2):
        next_row, next_column = cur_row, cur_column - i  # Движение влево от тек. позиции

        if labyrinth[next_row][next_column] == 2:  # Если встречаем 2, выводим кол-во ходов
            print(visited[(cur_row, cur_column)] + 1)
            exit()

        # Если встречаем 1 - аналогично:
        elif labyrinth[next_row][next_column] == 1:
            if (next_row, next_column + 1) not in visited:
                visited[(next_row, next_column + 1)] = visited[(cur_row, cur_column)] + 1
                queue.append((next_row, next_column + 1))
                break
            else:
                break

    for i in range(1, n + 2):  # Движение вверх от тек. позиции
        next_row, next_column = cur_row - i, cur_column

        if labyrinth[next_row][next_column] == 2:  # Если встречаем 2, выводим кол-во ходов
            print(visited[(cur_row, cur_column)] + 1)
            exit()

        elif labyrinth[next_row][next_column] == 1:  # Если встречаем 1, обрабатываем
            if (next_row + 1, next_column) not in visited:
                visited[(next_row + 1, next_column)] = visited[(cur_row, cur_column)] + 1
                queue.append((next_row + 1, next_column))
                break
            else:
                break

    for i in range(1, n + 2):  # Движение вниз от тек. позиции
        next_row, next_column = cur_row + i, cur_column

        if labyrinth[next_row][next_column] == 2:  # Если встречаем 2, выводим кол-во ходов
            print(visited[(cur_row, cur_column)] + 1)
            exit()

        elif labyrinth[next_row][next_column] == 1:  # Если встречаем 1, обрабатываем
            if (next_row - 1, next_column) not in visited:
                visited[(next_row - 1, next_column)] = visited[(cur_row, cur_column)] + 1
                queue.append((next_row - 1, next_column))
                break
            else:
                break
