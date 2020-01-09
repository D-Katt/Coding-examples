# Longest Palindromic Substring
# Given a string s, find the longest palindromic substring in s.
# You may assume that the maximum length of s is 1000.
# Example 1:
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example 2:
# Input: "cbbd"
# Output: "bb"


def palindrome(s):
    """Функция проверяет, является ли строка s палиндромом
    и возвращает True - если да и False - если нет."""
    end = len(s)
    middle = end // 2
    for i in range(middle):
        if s[i] != s[end - 1 - i]:
            return False
    return True


string = input()  # Считываем строку

letters = len(string)  # Определяем количество букв

iterations = 0  # Счетчик будет показывать, сколько раз
# подстрока заданной длины помещается внутри строки.

# Перебираем подстроки по убыванию длины - от максимальной,
# включающей всю исходную строку, до подстроки в одну букву.
for i in range(letters - 1, 0, -1):

    start = 0  # Начало подстроки в текущей строке.
    iterations += 1  # Количество разных подстрок такой длины.

    for j in range(iterations):

        # Вычленяем подстроку длины i, начиная от стартовой позиции.
        substring = string[start:start + i]

        # Проверяем, является ли подстрока палиндромом.
        result = palindrome(substring)

        if result:  # Если да, то выводим подстроку и завершаем программу.
            print(substring)
            exit()

        # Если нет - то смещаем стартовую позицию на 1.
        start += 1
