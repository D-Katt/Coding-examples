# Дан массив N × M. Требуется транспонировать его, т.е. обратить таблицу:
# строки становятся столбцами, столбцы - строками, вертикальная таблица становится горизонтальной и наоборот.
# Ширину и длину массива, а также значения элементов вводит пользователь.

n = int(input("Введите количество строк в массиве:\n"))
m = int(input("Введите количество столбцов в массиве:\n"))

A = [0] * n

print("Введите данные массива построчно, разделяя значения внутри строк пробелами:")

for i in range(n):
    A[i] = [int(s) for s in input().split()]

new_A = [[0] * n for i in range(m)]

for i in range(n):
    for j in range(m):
        new_A[j][i] = A[i][j]

for row in new_A:
    for el in row:
        print(str(el).rjust(3), end=' ')
    print()