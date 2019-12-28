# Нахождение кратчайшего цикла в ориентированном невзвешенном графе.
# Дан ориентированный граф. Вершины пронумерованы от 0.
# Трeбуется с помощью обхода в ширину найти цикл минимальной длины.
# На вход программе в первой строке подаются через пробел два числа:
# n (2 <= n <= 1000) - число вершин в графе.
# m (1 <= m <= 20000) - число ребер.
# В следующих m строках задаются ребра, по два числа в каждой строке -
# номера соединенных вершин (соответствующее ребро идет из первой вершины во вторую).
# Требуется распечатать номера вершин, задающих минимальный цикл в графе.
# Номера вершин нужно вывести в порядке следования по циклу.
# Если минимальных циклов несколько вывести любой.
# Если циклов нет вывести строку "NO CYCLES" без кавычек.

from collections import deque


def BFS(s, adj):
    """Функция обеспечивает BFS-обход графа от вершины s.
    adj - словарь смежности графа."""
    level = {s: 0}  # Словарь расстояний (уровней)
    # удаленности от стартовой вершины s.
    parent = {s: None}  # Словарь предшествующих вершин.
    i = 1  # Счетчик уровней удаленности от стартовой вершины.
    frontier = [s]  # Список содержит все вершины текущего рассматриваемого уровня.
    while frontier:
        next_v = []
        for u in frontier:  # Перебираем все вершины текущего уровня.
            for v in adj[u]:  # Для каждой перебираем смежные.
                if v not in level:  # Если их уровень еще не указан,
                    level[v] = i  # вносим их в словарь удаленности,
                    parent[v] = u  # в словарь предшествующих вершин,
                    next_v.append(v)  # добавляем в список для разбора на следующем уровне.
                else:  # Если стартовая вершина встретилась второй раз,
                    if v == s:  # то найден цикл.
                        parent[v] = u  # Указываем предшественника стартовой вершины в цикле.
                        return v, parent  # Функция возвращает вершину,
                        # входящую в цикл, и словарь предшественников.
        frontier = next_v  # Передаем список вершин следующего уровня в переменную frontier.
        i += 1  # Увеличиваем счетчик уровней удаленности на 1.
    return None, parent  # Если циклов не найдено, возвращается только словарь предшественников
    # и пустое значение циклической вершины.


n, m = (int(s) for s in input().split())  # Число вершин и ребер в графе.

graph = {i: set() for i in range(n)}  # Словарь множеств для хранения графа.

for i in range(m):  # Считываем ребра и добавляем в граф.
    a, b = (int(s) for s in input().split())
    graph[a].add(b)

cycles = []  # Список для хранения списков вершин, образующих циклы.

used = set()  # Множество использованных (вошедших в циклы) вершин,
# используется для того, чтобы избежать повторного нахождения тех же циклов.

for i in range(n):  # Перебираем все вершины графа.
    if i not in used:  # Если текущая вершина не включена в предыдущие найденные циклы,
        cycle_v, previous = BFS(i, graph)  # запускаем от нее BFS.
        if cycle_v:  # Если в процессе обхода данная вершина встретилась дважды,
            # то функция вернет непустое значение cycle_v.
            cur_cycle = deque([cycle_v])  # Очередь для восстановления текущего цикла.
            pr_v = previous[cycle_v]  # Предшествующая вершина.
            while pr_v != cycle_v:
                cur_cycle.appendleft(pr_v)
                pr_v = previous[pr_v]
            cycles.append(list(cur_cycle))  # Добавляем текущий цикл в список всех циклов.
            used = used.union(set(cur_cycle))  # Добавляем все вершины этого цикла
            # в множество использованных, чтобы избежать запуска BFS из них.

if not cycles:
    print("NO CYCLES")
    exit()

cycles.sort(key=lambda x: len(x))  # Сортируем список по длине подсписков.

# Выводим вершины самого короткого цикла.
for vertex in cycles[0]:
    print(vertex, end=" ")
