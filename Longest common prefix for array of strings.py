# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
# Example 1:
# Input: ["flower","flow","flight"]
# Output: "fl"
# Example 2:
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# Note:
# All given inputs are in lowercase letters a-z.

from sys import maxsize

# Считываем строки и преобразуем их в список строк:
strings = input().split()

# Определяем количество строк:
strings_num = len(strings)

# Создаем двумерную матрицу для дальнейшего преобразования списка строк.
string_matrix = [0] * strings_num

# Переменная для определения ширины матрицы, то есть длины самой короткой строки.
# Перед запуском цикла задаем ей максимально возможное значение.
width = maxsize

# Каждую строку разбиваем на буквы и добавляем список букв
# в матрицу под соответствующим индексом:
for i in range(len(strings)):
    string_matrix[i] = list(strings[i])

    # Вычисляем длину списка букв (т.е. ширину текущей строки матрицы)
    # и, при необходимости, обновляем переменную width.
    if len(string_matrix[i]) < width:
        width = len(string_matrix[i])

# Создаем переменную для добавления букв общего префикса:
prefix = ''

flag = True  # Переменная для определения (не)равенства букв
# i-й позиции всех строк матрицы после завершения цикла.
# До запуска циклов перебора присваиваем ей значение True.

# Перебираем элементы матрицы сначала по индексам столбцов, потом - строк.
for i in range(width):
    if not flag:  # Если на предыдущей итерации буквы были неодинаковы,
        break  # дальнейший перебор не требуется.

    # Переменная для хранения буквенного символа i-й позиции первой строки.
    previous = None

    for j in range(strings_num):
        current = string_matrix[j][i]  # Значение текущего элемента.

        if previous == None:  # Если значение переменной previous не определено,
            previous = current  # задаем его равным текущему элементу.

        else:  # Если переменная previous уже имеет значение,
            if previous != current:  # сравниваем его с текущим элементом.
                flag = False  # Если они разные, меняем значение переменной flag
                break  # и прерываем цикл.

    if flag:  # Если переменная flag имеет значение True, все i-е элементы всех строк одинаковы.
        prefix += current  # Добавляем текущий элемент в общий префикс.

# Выводим общий префикс:
print(prefix)
