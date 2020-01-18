# Trapping Rain Water. Given n non-negative integers representing an elevation map
# where the width of each bar is 1, compute how much water it is able to trap after raining.

#  3\       X
#  2\   X111XX1X
#  1\_X1XX1XXXXXX
#  0

# The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
# In this case, 6 units of rain water are being trapped.
# Example:
# Input: [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6

# Считываем последовательность высот:
array = [int(s) for s in input().split()]

# Для хранения данных мы будем использовать двумерный массив:
# количество чисел в списке array будет соответствовать количеству столбцов,
# количество строк - высоте самой высокой точки ландшафта.

# Находим максимальное значение в списке array (самая высокая точка на карте высот):
height = max(array)

# Создаем двумерный массив, заполняя его нулями.
# Предусматриваем дополнительный столбец для удобства расчетов:
height_map = [[0] * (len(array) + 1) for _ in range(height)]

# В каждом i-м столбце заменяем соответствующее число нулей на '*':
for i in range(len(array)):
    cur_height = array[i]
    for j in range(cur_height):
        height_map[j][i] = '*'

# Для наглядности можно визуализировать исходные данные и вывести их на экран:
for row in range(height - 1, -1, -1):
    for item in height_map[row]:
        print(str(item).rjust(5), end=' ')
    print()

total = 0  # Счетчик общего объема воды

for row in height_map:

    count = 0  # Счетчик объема воды в текущем "ряду"

    flag = -1  # Переменная для определения статуса счетчика,
    # Имеет два значения: 1 - счетчик активек, -1 - не активен.

    # Перебираем элемента текущего ряда:
    for j in range(len(row)):

        if flag == 1:  # Если счетчик активен,

            if row[j] == '*':  # и мы встречаем '*',
                total += count  # добавляем текущий объем воды к переменной total,
                count = 0  # обнуляем текущий счетчик.

                if row[j + 1] == '*':  # Если следующий символ также '*',
                    flag = -flag  # меняем статус переменной flag.

            else:  # row[j] == 0
                count += 1  # Если счетчик активен, и мы встречаем 0, увеличиваем счетчик.

        else:  # flag == -1
            if row[j] == '*' and row[j + 1] == 0:  # Если счетчик неактивен, и мы встречаем '*',
                flag = -flag  # за которой идет 0, меняем статус переменной flag.

print('Units of water =', total)  # Выводим полученный результат
