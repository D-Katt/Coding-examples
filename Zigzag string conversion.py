# Zigzag string conversion
# The string "PAYPALISHIRING" is written in a zigzag pattern
# on a given number of rows like this:
# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
# Write the code that will take a string and make this conversion given a number of rows:
# Example 1:
# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
# Example 2:
# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# P     I    N
# A   L S  I G
# Y A   H R
# P     I

from collections import deque

# Считываем строку и преобразуем ее в очередь:
string = deque(input())

# Считываем количество рядов:
rows = int(input())

# Список строк для преобразования исходной строки:
conversion = [''] * rows

# Сохраняем в список строк первый элемент исходной строки под индексом 0:
conversion[0] += string.popleft()
# (Это необходимо для того, чтобы на первой итерации
# шаг не поменялся на противоположный.)

pos = 0  # Указатель на текущий индекс в списке строк
step = 1  # Величина шага на следующей итерации

while string:  # Пока в очереди есть элементы,
    pos += step  # смещаем указатель на 1 шаг.
    # Если достигли 0-го или последнего элемента в списке строк,
    if pos == 0 or pos == rows - 1:
        step = -step  # меняем шаг на противоположный,
        # чтобы на следующей итерации двигаться в обратную сторону.
    conversion[pos] += string.popleft()  # Извлекаем первый элемент из очереди
    # и добавляем его к строке, находящейся в списке под текущим индексом.

# Выводим полученный список строк в одну строку:
for row in conversion:
    print(row, end='')
