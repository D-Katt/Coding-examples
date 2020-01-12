# Container With Most Water
# Given n non-negative integers a1, a2, ..., an , where each represents a point
# at coordinate (i, ai). n vertical lines are drawn such that the two endpoints
# of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis
# forms a container, such that the container contains the most water.
# Note: You may not slant the container and n is at least 2.
# Example:
# Input: [1,8,6,2,5,4,8,3,7]
# Output: 49
#
#     \______________\______
#     \              \     \
#     \  \           \     \
#     \  \     \     \     \
#     \  \     \  \  \     \
#     \  \     \  \  \  \  \
#     \  \  \  \  \  \  \  \
#  \  \  \  \  \  \  \  \  \
#  0  1  2  3  4  5  6  7  8


# Считываем последовательность координат (высоту линий):
points = [int(s) for s in input().split()]

# Используем переменную max_volume для нахождения максимального объема.
# Перед запуском цикла присваиваем ей значение 0.
max_volume = 0

# Перебираем элементы последовательности двумя циклами
# для нахождения максимального объема:
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        # Для каждой следующей комбинации двух координат находим объем,
        # т.е. умножаем наименьшую координату на расстрояние между двумя координатами.
        new_volume = min(points[i], points[j]) * (j - i)
        if new_volume > max_volume:  # Если расчетный объем превышает предыдущий максимум,
            max_volume = new_volume  # обновляем максимум.

print(max_volume)  # Выводим наибольший возможный объем.
