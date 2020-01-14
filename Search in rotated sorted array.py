# Search in Rotated Sorted Array. Suppose an array sorted in ascending order
# is rotated at some pivot unknown to you beforehand.
# (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
# You are given a target value to search. If found in the array
# return its index, otherwise return -1.
# You may assume no duplicate exists in the array.
# Your algorithm's runtime complexity must be in the order of O(log n).
# Example 1:
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1

from collections import deque

# Считываем последовательность чисел и преобразуем ее в очередь:
nums = deque([int(s) for s in input().split()])

# Считываем искомое число:
target = int(input())

# Переменная для расчета величины смещения (сдвига) массива чисел:
pivot = 0

# Количество чисел в последовательности:
end = len(nums)

# Перебираем числа одновременно с начала и с конца последовательности.
# Ищем точку, в которой минимальное значение следует за максимальным.
for i in range(end // 2):
    if nums[i] > nums[i + 1]:
        pivot = -i - 1
        break
    if nums[end - 1 - i] < nums[end - 2 - i]:
        pivot = i + 1
        break

# Сдвигаем все элементы очереди для восстановления исходной
# возрастающей последовательности чисел:
nums.rotate(pivot)

# Запускаем для исходной последовательности классический алгоритм
# бинарного поиска в массиве.


def left_bound(A, key):
    """Функция ищет элемент key в упорядоченном по возрастанию массиве А
    и возвращает индекс первого меньшего по значению элемента массива,
    в том числе в тех случаях, когда искомого элемента в массиве нет."""
    left = -1
    right = len(A)
    while right - left > 1:  # Поиск левой границы.
        middle = (left + right) // 2
        if A[middle] < key:
            left = middle
        else:
            right = middle
    return left


def right_bound(A, key):
    """Функция ищет элемент key в упорядоченном по возрастанию массиве А
    и возвращает индекс первого большего по значению элемента массива,
    в том числе в тех случаях, когда искомого элемента в массиве нет."""
    left = -1
    right = len(A)
    while right - left > 1:  # Поиск правой границы.
        middle = (left + right) // 2
        if A[middle] <= key:
            left = middle
        else:
            right = middle
    return right


# Находим левую и правую границы для искомого значения target
# в отсортированном массиве чисел nums.
left = left_bound(nums, target)
right = right_bound(nums, target)

if -1 <= left - right <= 1:  # Если индексы левой и правой границы
    print(-1)  # отличаются меньше чем на 1, элемента в массиве нет.

else:  # Если индекс левой границы отличается от правой больше чем на 1,
    # выводим результат с поправкой на смещение.
    if pivot > 0:
        print(left + 1 + end - pivot)
    else:
        print(left + 1 - pivot)
