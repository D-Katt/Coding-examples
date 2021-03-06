# В кинотеатре n рядов по m мест в каждом. В двумерном массиве хранится информация о проданных билетах,
# число 1 означает, что билет на данное место уже продан, число 0 означает, что место свободно.
# Поступил запрос на продажу k билетов на соседние места в одном ряду. Определите, можно ли выполнить такой запрос.
# Программа получает на вход числа n и m. Далее идет n строк, содержащих m чисел (0 или 1), разделенных пробелами.
# Затем дано число k.
# Программа должна вывести номер ряда, в котором есть k подряд идущих свободных мест.
# Если таких рядов несколько, то выведите номер наименьшего подходящего ряда.
# Если подходящего ряда нет, выведите число 0.

n, m = (int(s) for s in input().split())  # Кол-во рядов и мест в ряду

A = [0] * m

for i in range(n):
    A[i] = [int(s) for s in input().split()]  # Считываем данные о проданных местах рядами

k = int(input())  # Требуемое кол-во мест, расположенных рядом

row = 0
c = 0

for i in range(n):
    for j in range(m):
        if A[i][j] == 0:
            c += 1
            if c == k:
                row = i + 1
                break
        else:
            c = 0

print(row)
