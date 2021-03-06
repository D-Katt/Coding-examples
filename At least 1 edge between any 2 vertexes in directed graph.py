# Ориентированный граф называется полуполным, если между любой парой
# его различных вершин есть хотя бы одно ребро. Для заданного списком ребер
# графа проверьте, является ли он полуполным.
# Сначала вводятся числа n ( 1 <= n <= 100) – количество вершин в графе
# и m ( 1 <= m <= n(n - 1)) – количество ребер. Затем следует m пар чисел –
# ребра графа. Номера вершин начинаются с 0.
# Выведите «YES», если граф является полуполным, и «NO» в противном случае.

from itertools import combinations

n, m = (int(s) for s in input().split())
# n - количество вершин, m - количество ребер

Graph = [[0] * n for _ in range(n)]  # Заготовка под матрицу смежности

for i in range(m):  # Считываем ребра попарно
    a, b = (int(s) for s in input().split())
    Graph[a][b] += 1

vertexes = [i for i in range(n)]  # Список всех вершин для последующего перебора комбинаций

pairs = combinations(vertexes, 2)  # Список комбинаций всех вершин

for a, b in pairs:
    if Graph[a][b] + Graph[b][a] < 1:  # Проверяем наличие хотя бы одной связи
        print("NO")  # в каждой комбинации вершин.
        exit()

print("YES")
