# Нахождение вершины-столицы. В некотором государстве некотрые города соединены дорогами.
# Жители этого государства просят вас помочь им с выбором столицы: требуется,
# чтобы сумма расстояний от столицы до каждого из остальных городов была минимальна.
# Для вашего удобства города уже пронумерованы от 0 до n-1.
# Формат входных данных
# На вход программе в первой строке подается два числа через пробел: n и m.
# n (2 <= n <= 100) - число городов, m (1 <= m <= 500) - число дорог.
# В следующих m строках задаются дороги, по три числа в каждой строке -
# номера соединенных городов и длина дороги.
# Формат выходных данных
# Выведите номер столицы. Если возможно несколько варинтов, выведете любой.

from sys import maxsize


class Graph():

	def __init__(self, vertices):
		self.V = vertices
		self.graph = [[0 for column in range(vertices)]
					for row in range(vertices)]

	def solution(self, dist, src):
		"""Функция вычисляет сумму расстояний от вершины src
		до всех остальных в списке dist и сохраняет результат
		в список min_distance под индексом src."""
		sum_dist = 0
		for node in range(self.V):
			sum_dist += dist[node]
			min_distance[src] = sum_dist

	def minDistance(self, dist, sptSet):
		"""Вспомогательная функция для поиска вершины с минимальным расстоянием
		среди множества вершин, еще не вошедших в кратчайший путь."""

		# Задаем мин. расстояние до следующего узла:
		min = maxsize

		# Просматриваем не ближайшие вершины, не входящие в кратчайший путь:
		for v in range(self.V):
			if dist[v] < min and sptSet[v] == False:
				min = dist[v]
				min_index = v

		return min_index

	def dijkstra(self, src):
		"""Функция запускает алгоритм Дейкстры для поиска кратчайшего расстояния
		в графе, представленном матрицей смежности."""

		dist = [maxsize] * self.V
		dist[src] = 0
		sptSet = [False] * self.V

		for cout in range(self.V):

			# Выбираем вершину с мин. расстоянием среди множества
			# не обработанных вершин. На первой итерации это src.
			u = self.minDistance(dist, sptSet)

			# Вносим вершину с мин. расстоянием в кратчайший путь.
			sptSet[u] = True

			# Обновляем значения смежных вершин в списке dist,
			# только если текущее расстояние больше нового
			# и вершина еще не в кратчайшем пути.
			for v in range(self.V):
				if self.graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + self.graph[u][v]:
					dist[v] = dist[u] + self.graph[u][v]

		self.solution(dist, src)


n, m = (int(s) for s in input().split())

# Двумерная матрица для хранения данных о длине дорог между городами.
# Перед считыванием графа задаем каждое расстояние макс. числом.
cities = [[0] * n for _ in range(n)]

for i in range(m):  # Вносим данные о длине существующих дорог в матрицу:
    c1, c2, distance = (int(s) for s in input().split())
    cities[c1][c2] = distance
    cities[c2][c1] = distance

# Создаем экземпляр класса граф с n вершинами
g = Graph(n)
# Передаем ему матрицу смежности
g.graph = cities

# Список для хранения суммы расстояний от каждой вершины до всех остальных.
min_distance = [None] * n

# Запускаем функцию поиска расстояний от каждой вершины:
for i in range(n):
    g.dijkstra(i)
    if i == 0:  # Сравниваем суммарные расстояния в поисках минимума:
        capital_distance = min_distance[0]
        capital_ind = 0
    else:
        if min_distance[i] < capital_distance:
            capital_distance = min_distance[i]
            capital_ind = i

print(capital_ind)  # Выводим индекс города с мин. расстояниями до остальных.
