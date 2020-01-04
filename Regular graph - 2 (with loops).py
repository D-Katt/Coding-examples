# Неориентированный граф называется регулярным, если все его вершины имеют одинаковую степень.
# Для заданного списком ребер графа проверьте, является ли он регулярным.
# Формат входных данных
# Сначала вводятся числа n ( 1 ≤ n ≤ 100) – количество вершин в графе
# и m ( 0 ≤ m ≤ n(n - 1)/2) – количество ребер.
# Затем следует m пар чисел – ребра графа. Нумерация вершин с 0.
# Формат выходных данных
# Выведите «YES», если граф является регулярным, и «NO» в противном случае.

# Программа корректно работает на любых неориентированных графах,
# в том числе содержащих петли - ребра, выходящие из и возвращающиеся
# в одну и ту же вершину. При подсчете степени ребро-петля учитывается дважды.

n, m = (int(s) for s in input().split())

# Граф в формате списка. Индекс элемента соответствует номеру вершины.
# Значение элемента соответствует ее степени.
graph = [0] * n

# Считываем ребра и увеличиваем степени соответствующих вершин в списке:
for i in range(m):
    a, b = (int(s) for s in input().split())
    graph[a] += 1
    graph[b] += 1

# Если в графе не более 2 вершин, то они в любом случае будут иметь одинаковую степень.
if 1 <= n <= 2:
    print('YES')
    exit()

# Перед запуском цикла сохраняем в переменную edges значение 0-го элемента списка
# (степень первой вершины графа).
edges = graph[0]

# Перебираем все оставшиеся вершины графа и сравниваем количество смежных:
for i in range(1, len(graph)):
    if graph[i] != edges:  # При первом же расхождении
        print('NO')  # завершаем программу.
        exit()

# Если мы перебрали вершины и не встретили расхождений в количестве смежных,
# то граф - регулярный.
print('YES')
