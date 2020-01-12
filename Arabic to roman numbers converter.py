# Integer to Roman
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, two is written as II in Roman numeral, just two one's added together.
# Twelve is written as, XII, which is simply X + II.
# The number twenty seven is written as XXVII, which is XX + V + II.
# Roman numerals are usually written largest to smallest from left to right.
# However, the numeral for four is not IIII. Instead, the number four is written as IV.
# Because the one is before the five we subtract it making four.
# The same principle applies to the number nine, which is written as IX.
# There are six instances where subtraction is used:
# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given an integer, convert it to a roman numeral.
# Input is guaranteed to be within the range from 1 to 3999.

# Считываем число:
number = int(input())

# Преобразуем число в список строк, т.е. разбиваем его на разряды:
number = str(number)

# Создаем пустой новый список для дальнейшего преобразования арабского числа:
number_list = []

# Перебираем элементы списка number от начала к концу,
# т.е. от самого большого разряда числа к самому маленькому:
for i in range(len(number)):
    digit = int(number[i])  # Каждый элемент преобразуем в число
    for j in range(len(number) - 1 - i):
        digit *= 10  # и соответствующее число раз умножаем на 10.
    number_list.append(digit)  # Добавляем полученное значение в список number_list.
    # Т.е. число 123 преобразуется в список [100, 20, 3]

# Создаем словарь для быстрой конвертации арабских цифр в буквенные символы римских чисел:
numbers = {1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX',
           10: 'X', 20: 'XX', 30: 'XXX', 40: 'XL', 50: 'L', 60: 'LX', 70: 'LXX', 80: 'LXXX', 90: 'XC',
           100: 'C', 200: 'CC', 300: 'CCC', 400: 'CD', 500: 'D', 600: 'DC', 700: 'DCC', 800: 'DCCC', 900: 'CM',
           1000: 'M', 2000: 'MM', 3000: 'MMM'}  # По условиям задачи число не превышает 3999.

# Создаем строку для добавления буквенных символов римского числа:
roman_number = ''

# Перебираем список number_list и последовательно добавляем
# к строке roman_number соответствующие символы римского числа:
for digit in number_list:
    roman_number += numbers[digit]

# Выводим полученное римское число:
print(roman_number)
