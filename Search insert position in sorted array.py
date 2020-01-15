# Search Insert Position. Given a sorted array and a target value,
# return the index if the target is found. If not, return the index
# where it would be if it were inserted in order.
# You may assume no duplicates in the array.
# Example 1:
# Input: [1,3,5,6], 5
# Output: 2
# Example 2:
# Input: [1,3,5,6], 2
# Output: 1
# Example 3:
# Input: [1,3,5,6], 7
# Output: 4
# Example 4:
# Input: [1,3,5,6], 0
# Output: 0

# Считываем последовательность чисел:
sequence = [int(s) for s in input().split()]

# Считываем искомое значение:
target = int(input())

# Так как последовательность упорядочена по возрастанию,
# для поиска позиции вставки элемента подойдет классический алгоритм
# бинарного поиска в массиве. При этом достаточно найти только левую границу.


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


# Находим левую границу для искомого значения target
# в упорядоченном массиве чисел sequence.
left = left_bound(sequence, target)

# Выводим результат, увеличив индекс на 1.
print(left + 1)
