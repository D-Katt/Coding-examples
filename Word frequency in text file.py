# Write a code to calculate the frequency of each word in a text file.
# The file contains only lowercase characters and space ' ' characters.
# Each word must consist of lowercase characters only.
# Words are separated by one or more whitespace characters.
# Output should be sorted by descending frequency.

from collections import defaultdict
from operator import itemgetter

# Создаем словарь для подсчета частоты слов:
words = defaultdict(int)

# Считываем из файла по одной строке, пока не достигнем конца файла.
with open('text', 'r') as t:
    while True:
        line = t.readline()
        if not line:  # Если очередная строка не содержит символов, прерываем цикл.
            # Если внутри текстового файла есть пустые строки (без текста),
            # цикл на них не прервется, т.к. пустая строка
            # содержит символ перевода строки. Весь текст до конца файла будет прочитан.
            break
        line = line.split()  # Преобразуем строку в список слов.
        for word in line:  # Добавляем их в словарь / увеличиваем частоту.
            words[word] += 1

words_list = []

# Преобразуем словарь в список кортежей:
for key, value in words.items():
    words_list.append((key, value))

# Сортируем по второму элементу в кортежах - по убыванию частоты.
words_list.sort(key=itemgetter(1), reverse=True)

# Выводим построчно (слово + частота):
for word, number in words_list:
    print(word, number)
