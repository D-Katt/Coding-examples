# Tenth Line
# Given a text file file.txt, print just the 10th line of the file.
# Example:
# Assume that file.txt has the following content:
# Line 1
# Line 2
# Line 3
# Line 4
# Line 5
# Line 6
# Line 7
# Line 8
# Line 9
# Line 10
# Line 11
# Your script should output the tenth line, which is:
# Line 10
# Note:
# 1. If the file contains less than 10 lines, what should you output?
# 2. There's at least three different solutions. Try to explore all possibilities.

from itertools import islice

with open('text', 'r') as t:
    # Используем файл как итератор, срез ограничен элементом с индексом 9
    # (10-я строка).
    lines = islice(t, 9, 10)

    flag = True  # Переменная служит индикатором того,
    # удалось ли считать 10-ю строку из файла.

    for line in lines:
        if line:  # Если полученный итератор содержит непустую строку,
            flag = False  # меняем значение переменной flag,
            print(line)  # выводим строку.

    # Если значение переменной flag не поменялось,
    # выводим сообщение об ошибке:
    if flag:
        print("Fail: the file contains less than 10 lines.")

# Примечание. Если в файле не менее 10 строк, но 10-я строка не содержит
# печатаемых символов, программа выведет пустую строку без сообщения об ошибке.
