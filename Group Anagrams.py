# Group Anagrams. Given an array of strings, group anagrams together.
# Example:
# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
# Note: All inputs will be in lowercase.
# The order of your output does not matter.

# Считываем последовательность слов:
words = [word for word in input().split()]

# Список для добавления подсписков из слов-анаграмм:
anagrams = []

# Словарь букв, хранящихся по индексам в списке 'anagrams':
anagram_ind = dict()

# Перебираем слова в исходном списке.
for word in words:

    # Смотрим на длину текущего списка анаграмм.
    length = len(anagrams)

    if length == 0:  # Если в анаграммах нет значений,
        anagrams.append([word])  # добавляем в список текущее слово
        anagram_ind[0] = set(word)  # и создаем из него множество букв под индексом 0.

    else:  # Если в анаграммах есть значения,
        cur_word = set(word)  # преобразуем текущее слово в множество букв.

        # Создаем переменную для проверки наличия такого же множества в словаре:
        flag = False

        # Перебираем множества букв в словаре по ключам-индексам:
        for i in range(length):
            # Если текущее множество совпало с одним из имеющихся в словаре,
            if anagram_ind[i] == cur_word:
                # добавляем текущее слово в подсписок анаграмм под соответствующим индексом.
                anagrams[i].append(word)
                # Меняем значение переменной flag и прерываем цикл поиска совпадений.
                flag = True
                break

        # Если после завершения цикла переменная flag не поменяла значение,
        # значит, в словаре не было аналогичных множеств букв.
        if not flag:
            # Добавляем текущее слово в конец списка анаграмм в качестве самостоятельного подсписка.
            anagrams.append([word])
            # Создаем в словаре новое множество букв под индексом текущего слова.
            anagram_ind[length] = cur_word

# Выводим полученные списки анаграмм:
for anagram in anagrams:
    print(anagram)
