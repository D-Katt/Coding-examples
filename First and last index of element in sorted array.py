# Find First and Last Position of Element in Sorted Array.
# Given an array of integers nums sorted in ascending order,
# find the starting and ending position of a given target value.
# Your algorithm's runtime complexity must be in the order of O(log n)
# If the target is not found in the array, return [-1, -1].
# Example 1:
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]

# Считываем последовательность чисел:
sequence = [int(s) for s in input().split()]

# Считываем искомое значение:
target = int(input())

# Так как последовательность упорядочена по возрастанию, для поиска элемента
# подойдет классический алгоритм бинарного поиска в массиве.


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
# в упорядоченном массиве чисел sequence.
left = left_bound(sequence, target)
right = right_bound(sequence, target)

if -1 <= left - right <= 1:  # Если индексы левой и правой границы
    print(-1, -1)  # отличаются меньше чем на 1, элемента в массиве нет.

else:  # Если индекс левой границы отличается от правой больше чем на 1,
    # выводим результат с поправкой на 1.
    print(left + 1, right - 1)
