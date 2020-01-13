# 3Sum. Given an array nums of n integers, are there elements a, b, c in nums
# such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
# Note: The solution set must not contain duplicate triplets.
# Example:
# Given array nums = [-1, 0, 1, 2, -1, -4],
# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]

# Считываем последовательность чисел:
nums = [int(s) for s in input().split()]

# Количество чисел в последовательности:
limit = len(nums)

# Множество возможных наборов из трех чисел:
solutions = set()

# Перебираем элементы последовательности тремя вложенными циклами.
# Индекс стартовой позиции каждого следующего цикла на 1 больше предыдущего.
for i in range(limit):
    for j in range(i + 1, limit):
        for z in range(j + 1, limit):
            if nums[i] + nums[j] + nums[z] == 0:
                # Элементы последовательности не упорядочены и среди них
                # могут встречаться одинаковые числа. Поэтому при нахождении
                # очередной комбинации, дающей в сумме 0, необходимо проверить,
                # что такой набор чисел не встречался раньше.
                # Составляем список из трех найденных чисел и сортируем его.
                cur_combination = [nums[i], nums[j], nums[z]]
                cur_combination.sort()
                # Если такой набор чисел в возрастающей последовательности
                # не встречался раньше, добавляем его в множество solutions.
                cur_combination = tuple(cur_combination)
                if cur_combination not in solutions:
                    solutions.add(cur_combination)

# Выбодим возможные варианты сочетаний цифр:
for solution in solutions:
    for number in solution:
        # Для улучшения визуального восприятия итоговых данных
        # выравниваем цифры по правому краю и добавляем пробелы.
        print(str(number).rjust(8), end=' ')
    print()
