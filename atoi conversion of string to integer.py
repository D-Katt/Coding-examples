# Implement atoi which converts a string to an integer.
# The function first discards as many whitespace characters as necessary
# until the first non-whitespace character is found. Then, starting from
# this character, takes an optional initial plus or minus sign followed
# by as many numerical digits as possible, and interprets them as a numerical value.
# The string can contain additional characters after those that form
# the integral number, which are ignored and have no effect
# on the behavior of this function.
# If the first sequence of non-whitespace characters in str is not
# a valid integral number, or if no such sequence exists because
# either str is empty or it contains only whitespace characters,
# no conversion is performed.
# If no valid conversion could be performed, a zero value is returned.
# Note:
# Only the space character ' ' is considered as whitespace character.
# Assume we are dealing with an environment which could only store integers
# within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value
# is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.
# Example 1:
# Input: "42"
# Output: 42
# Example 2:
# Input: "   -42"
# Output: -42
# Explanation: The first non-whitespace character is '-', which is the minus sign.
#              Then take as many numerical digits as possible, which gets 42.
# Example 3:
# Input: "4193 with words"
# Output: 4193
# Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.
# Example 4:
# Input: "words and 987"
# Output: 0
# Explanation: The first non-whitespace character is 'w', which is not a numerical
#              digit or a +/- sign. Therefore no valid conversion could be performed.
# Example 5:
# Input: "-91283472332"
# Output: -2147483648
# Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
#              Thefore INT_MIN (−231) is returned.


from sys import maxsize


def atoi_conversion(s: str):
    """Функция преобразует строку s, содержащую произвольный набор символов,
    в целое число. Возвращает 0, если строка пуста, если в строке нет цифр,
    если буквы и др. символы предшествуют цифрам. Если полученное число превышает
    размер +/-maxsize, возвращает сооветствующее значение maxsize."""

    # Переменная для добавления цифр числа, найденного в строке.
    number = ''

    # Переменная, которая будет сигнализировать, что перед числом стоял '-'.
    sign = False

    # Переменная будет сигнализировать, что предыдущие элементы строки были цифрами.
    check = False

    for i in range(len(s)):
        # Если встретили в строке буквенные и др. символы до цифр,
        # преобразование невозможно.
        if not check and s[i] not in '0123456789 -':
            return 0

        # Если переменная 'check' имеет значение True и очередной элемент не цифра,
        # значит, необходимо прервать перебор, т.к. мы считали число из строки
        # и снова начались буквы и символы, которые необходимо отбросить.
        if check and s[i] not in '0123456789':
            break
        # Если в строке встретился '-', за которым стоит цифра, и до него цифр не было,
        # меняем значение переменной 'sign'.
        if s[i] == '-' and s[i + 1] in '0123456789' and not check:
            sign = True
        # Если в строке встретилась цифра, добавляем ее в переменную 'number'
        # и меняем значение переменной 'check'.
        if s[i] in '0123456789':
            number += s[i]
            check = True

    # Если мы перебрали все элементы строки и не встретили цифр,
    # преобразование невозможно.
    if not number:
        return 0

    # Преобразуем подстроку, содержащую цифры, в число с соответствующим знаком:
    if sign:
        number = -int(number)
    else:
        number = int(number)

    # Если число превышает положительный или отрицательный максимум,
    # возвращаем соответствующий максимум.
    if number > maxsize:
        return maxsize
    elif number < -maxsize:
        return -maxsize
    else:  # Если число в допустимом диапазоне значений, возвращаем число.
        return number


# Считываем строку, содержащую цифры, буквы, пробелы и др. символы.
string = input()

# Выводим результат преобразования:
print(atoi_conversion(string))
