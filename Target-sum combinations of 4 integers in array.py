# 4Sum. Given an array nums of n integers and an integer target,
# are there elements a, b, c, and d in nums such that a + b + c + d = target?
# Find all unique quadruplets in the array which gives the sum of target.
# Note: The solution set must not contain duplicate quadruplets.
# Example:
# Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.
# A solution set is:
# [
#   [-1,  0, 0, 1],
#   [-2, -1, 1, 2],
#   [-2,  0, 0, 2]
# ]

# Считываем последовательность чисел:
nums = [int(s) for s in input().split()]

# Считываем искомую сумму:
target = int(input())

# Количество чисел в последовательности:
limit = len(nums)

# Множество возможных наборов из четырех чисел:
solutions = set()

# Перебираем элементы последовательности четырьмя вложенными циклами.
# Индекс стартовой позиции каждого следующего цикла на 1 больше предыдущего.
for i in range(limit):
    for j in range(i + 1, limit):
        for z in range(j + 1, limit):
            for x in range(z + 1, limit):
                if nums[i] + nums[j] + nums[z] + nums[x] == target:
                    # Элементы последовательности не упорядочены, и среди них
                    # могут встречаться одинаковые числа. Поэтому при нахождении
                    # очередной комбинации, дающей искомую сумму,
                    # необходимо проверить, что такой набор чисел не встречался раньше.
                    # Составляем список из четырех найденных чисел и сортируем его.
                    cur_combination = [nums[i], nums[j], nums[z], nums[x]]
                    cur_combination.sort()
                    # Если такой набор чисел в возрастающей последовательности
                    # не встречался раньше, добавляем его в множество solutions.
                    cur_combination = tuple(cur_combination)
                    if cur_combination not in solutions:
                        solutions.add(cur_combination)

# Выбодим возможные варианты сочетаний чисел:
for solution in solutions:
    for number in solution:
        # Для улучшения визуального восприятия итоговых данных
        # выравниваем числа по правому краю и добавляем пробелы.
        print(str(number).rjust(8), end=' ')
    print()
