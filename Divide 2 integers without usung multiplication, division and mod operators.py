# Given two integers dividend and divisor, divide two integers
# without using multiplication, division and mod operator.
# Return the quotient after dividing dividend by divisor.
# The integer division should truncate toward zero.
# Example 1:
# Input: dividend = 10, divisor = 3
# Output: 3
# Example 2:
# Input: dividend = 7, divisor = -3
# Output: -2
# Note:
# Both dividend and divisor will be 32-bit signed integers.
# The divisor will never be 0.
# Assume we are dealing with an environment which could only store integers
# within the 32-bit signed integer range: [−231,  231 − 1].
# For the purpose of this problem, assume that your function
# returns 231 − 1 when the division result overflows.

from sys import maxsize

# Считываем делимое:
dividend = int(input())
# Считываем делитель:
divisor = int(input())

# Переменная для подсчета числа вхождений делителя в делимое:
count = 0

# В зависимости от того, какой знак имеют рассматриваемые числа,
# последовательно вычитаем или прибавляем делитель к делимому,
# пока делимое не пересечет 0 в ту или другую сторону.
# Подчитываем количество операций сложения и вычитания соответственно.
# Выводим переменную count, уменьшив ее на 1 и добавив соответствующий знак.
if dividend >= 0:
    if divisor > 0:
        while dividend >= 0:
            dividend -= divisor
            count += 1
        count -= 1
    elif divisor < 0:
        while dividend >= 0:
            dividend += divisor
            count += 1
        count = -(count - 1)
else:  # dividend < 0
    if divisor < 0:
        while dividend <= 0:
            dividend -= divisor
            count += 1
        count -= 1
    elif divisor > 0:
        while dividend <= 0:
            dividend += divisor
            count += 1
        count = -(count - 1)

# Выводим результат деления. Если он превышает максимальный размер числа,
# выводим соответствующее сообщение.
if count >= maxsize:
    print('Maximum integer number exceeded. Result = +INF')
elif count <= - maxsize:
    print('Maximum integer number exceeded. Result = -INF')
else:
    print('Result =', count)

# На практике деление очень больших чисел на маленькие таким способом
# выполняется очень медленно, и результата можно не дождаться :(
