# Поиск расстояний от заданной вершины до всех остальных
# Дан невзвешенный неориентированный связный граф. Вершины пронумерованы от 0.
# Трeбуется с помощью обхода в ширину найти расстояния от 0-й до всех остальных вершин.
# Формат входных данных
# На вход программе в первой строке подаются через пробел два числа:
# n (2 <= n <= 1000) — число вершин в графе и m (1 <= m <= 20000) — число рёбер.
# В следующих m строках задаются ребра: по два числа в каждой строке — номера соединённых вершин.
# Формат выходных данных
# Требуется распечатать n чисел, каждое на новой строке. В первой строке —
# расстояния от 0-й вершины до 0-й, во второй - от 0-й до 1-й, в третьей — от 0-й до 2-й и т.д.

from collections import deque

n, m = (int(s) for s in input().split())

graph = {i: set() for i in range(n)}  # Словарь множеств для хранения графа.

for i in range(m):
    v1, v2 = map(int, input().split())  # Считываем ребро.
    graph[v1].add(v2)
    graph[v2].add(v1)

distances = [None] * n  # Массив расстояний от стартовой вершины до всех пройденных.
distances[0] = 0  # Присваиваем 0-й вершине значение 0 в списке distances.

queue = deque([0])  # Создаем очередь для перебора вершин.

while queue:  # Как только queue станет пустой, выполнение цикла прекратится.
    cur_v = queue.popleft()  # Добываем из очереди первый элемент.
    for neigh_v in graph[cur_v]:  # Перебираем его соседей.
        if distances[neigh_v] is None:  # Если соседнюю вершину не посещали,
            # она имеет значение None в списке distances.
            distances[neigh_v] = distances[cur_v] + 1  # Тогда присваиваем ей
            # значение ее предшествующей вершины + 1.
            queue.append(neigh_v)  # Добавляем эту вершину в конец очереди.

for distance in distances:
    print(distance)
