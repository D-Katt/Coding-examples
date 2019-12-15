# Пастбище представляет собой прямоугольник, разбитый на N x N клеток. В каждой клетке растет трава,
# имеющая свою калорийность (во всех клетках калорийность травы разная). В левой нижней клетке стоит корова.
# Съев всю траву в своей клетке, она перемещается на одну клетку вправо или на одну клетку вверх,
# всегда выбирая ту из клеток, калорийность травы в которой больше (за пределами поля трава не растет).
# В конце концов корова приходит в правую верхнюю клетку. Требуется определить, сколько всего калорий получит корова
# (считая калории травы в первой и в последней клетках).
# Сначала вводится число N – размер поля (2 ≤ N ≤ 10). В следующей строке вводятся через пробел числа,
# задающие количество калорий в клетках верхнего ряда, в следующей – количество калорий в клетках следующего ряда, …,
# в последней – количество калорий в клетках нижнего ряда. Все числа – различные, натуральные, не превосходящие 100.
# Требуется вывести количество калорий, которое получит корова.

N = int(input())  # Размеры квадратного поля
A = [[0] * 11 for s in range(11)]  # Т.к. 2 ≤ N ≤ 10, создаем массив с запасом в 1 клетку.

for i in range(11 - N, 11):
    row = input().split()
    for j in range(N):
        row[j] = int(row[j])
    A[i] = row + [0] * (11 - N)  # Клетки за пределами поля заполняем нулями.

line = 10
column = 0
calories = A[line][column]

while line > 0 and column < 10:
    if A[line-1][column] > A[line][column+1]:
        calories = calories + A[line-1][column]
        line -= 1
    else:
        calories = calories + A[line][column+1]
        column +=1

print(calories)
