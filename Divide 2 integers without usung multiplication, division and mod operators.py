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

# Операцию деления можно заменить на последовательные операции вычитания
# делителя из делимого с подсчетом количества итераций. Вычитание производится
# до тех пор, пока делимое не достигнет нуля.
# На практике деление очень больших чисел на маленькие таким способом
# выполняется очень медленно, и результата можно не дождаться :(
# Поэтому для таких случаев дополнительно введем поправку на разрядность делителя,
# чтобы максимально приблизить его к делимому. К полученному результату затем
# необходимо применить ту же поправку на разрядность.

# Вычисляем разницу в количестве знаков стрингифицированного делимого и делителя:
len_difference = len(str(dividend)) - len(str(divisor))

# Если преобразованное в строку делимое более чем на 3 знака превышает делитель,
# вводим поправку на разрядность (переменная correction).
if len_difference >= 3:
    correction = len_difference - 2
    # Пояснение. Поскольку результат деления округляется в сторону нуля,
    # мы не можем приплюсовать к делителю такое же количество разрядов,
    # как есть у делимого. Например, при делении 1000 на 9 добавление трех нулей
    # к делителю приведет к делению 1000 на 9000, что даст в результате ноль.
    # Если же мы разделим 1000 на 900 и потом прибавим к полученному результату 00,
    # то количество итераций сократится и получится правильный результат.
    # Еще один "запасной" разряд предусмотрен для тех случаев,
    # когда большое отрицательное число делится на маленьное положительное,
    # например, -1000 на 9.
else:
    correction = 0

zero = ''

if correction:  # Если переменная correction имеет значение, не равное нулю,
    divisor = str(divisor)  # преобразуем делитель в строку.
    for i in range(correction):  # Формируем строку zero из соответствующего кол-ва нулей.
        zero += '0'
    divisor += zero  # Прибавляем полученную строку из нулей к делителю,
    divisor = int(divisor)  # и преобразуем его в целое число.

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

if correction:  # Если переменная correction имеет значение, не равное нулю,
    # необходимо применить к переменной count поправку на разрядность,
    # аналогичную той, которая применялась выше к делителю.
    count = str(count)  # Преобразуем полученный результат в строку.
    count += zero  # Прибавляем к ней соответствующее количество нулей.
    count = int(count)  # Преобразуем результат обратно в целое число.

# Выводим результат деления. Если он превышает максимальный размер числа,
# выводим соответствующее сообщение.
if count >= maxsize:
    print('Maximum integer number exceeded. Result = +INF')
elif count <= - maxsize:
    print('Maximum integer number exceeded. Result = -INF')
else:
    print('Result =', count)
