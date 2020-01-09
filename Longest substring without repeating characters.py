# Given a string, find the length of the longest
# substring without repeating characters.

string = input()  # Считываем строку

maximum = 0  # Длина самой длинной подстроки.
cur_max = 0  # Длина текущей подстроки.

cur_substring = ''  # Текущая подстрока без повторяющихся символов.

cur_set = set()  # Текущее множество букв строки
# для быстрой проверки повторяющих элелементов.

for i in range(len(string)):  # Последовательно перебираем все символы строки.

    if string[i] not in cur_set:
        # Если очередной символ не встречался раньше,
        # добавляем его в очередь и в подстроку, увеличиваем cur_max.
        cur_set.add(string[i])
        cur_substring += string[i]
        cur_max += 1

        if cur_max > maximum:  # Если текущая строка длиннее предыдущего максимума,
            maximum = cur_max  # обновляем его.

    else:  # Если очередной символ уже встречался раньше,
        pos = cur_substring.find(string[i])  # находим его индекс в текущей подстроке,
        cur_substring = cur_substring[pos + 1:]  # отбрасываем все знаки до этого символа включительно,
        cur_substring += string[i]  # добавляем его в конец подстроки.
        cur_set = set(cur_substring)  # Обновляем содержимое текущего множества.
        cur_max = len(cur_set)  # Обновляем текущий максимум.

print(maximum)
