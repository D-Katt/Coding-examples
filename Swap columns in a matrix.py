# Дан двумерный массив и два числа: i и j. Поменяйте в массиве столбцы с номерами i и j и выведите результат.
# Программа получает на вход размеры массива n и m, затем элементы массива, затем числа i и j.
# Решение оформите в виде функции swap_columns(a, i, j).

n, m = (int(s) for s in input().split())  # Размеры массива

A = []

for i in range(n):
    A.append([int(s) for s in input().split()])  # Элементы массива вводятся построчно

i, j = (int(s) for s in input().split())  # Индексы перемещаемых столбцов


def swap(a, i, j):
    new = a
    for g in range(len(a)):
        new[g][i], new[g][j] = new[g][j], new[g][i]
    return new


B = swap(A, i, j)

for r in B:
    for el in r:
        print(el, end=' ')
    print()
