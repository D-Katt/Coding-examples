# First Missing Positive. Given an unsorted integer array,
# find the smallest missing positive integer.
# Example 1:
# Input: [1,2,0]
# Output: 3
# Example 2:
# Input: [3,4,-1,1]
# Output: 2
# Example 3:
# Input: [7,8,9,11,12]
# Output: 1
# Note: Your algorithm should run in O(n) time and uses constant extra space.

# Считываем последовательность чисел и преобразуем ее в множество:
numbers = set(int(s) for s in input().split())

counter = 1  # Переменная для последовательного поска положительных чисел.

while True:
    if counter not in numbers:  # Если очередной положительное число отсутствует в множестве,
        print(counter)  # выводим его на экран и прерываем цикл.
        break
    else:  # Если такое число есть в множестве, увеличиваем его на 1.
        counter += 1
