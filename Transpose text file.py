# Transpose File
# Given a text file file.txt, transpose its content.
# You may assume that each row has the same number of columns
# and each field is separated by the ' ' character.
# Example:
# If file.txt has the following content:
# name age
# alice 21
# ryan 30
# Output the following:
# name alice ryan
# age 21 30


with open('text', 'r') as t:
    # Считываем первую строку из файла:
    line = t.readline()
    # Преобразуем строку в список, разделяя слова по пробелам.
    line = line.split()
    # Создаем список списков для преобразования исходного текста.
    # Количество строк в нем соответствует количеству слов в исходной строке.
    trans_lines = [None] * len(line)
    # Перекладываем элементы первой строки поштучно в новый список по индексам:
    for i in range(len(line)):
        trans_lines[i] = [line[i]]
    # Считываем оставшиеся строки файла:
    while True:
        line = t.readline()
        if not line:  # Если достигли конца файла, в строке не будет символов.
            break  # В этом случае прерываем цикл.
        line = line.split()  # Преобразуем строку в список.
        # Добавляем элементы очередной строки к соответствующим им по индексу
        # подсписку списка trans_lines:
        for i in range(len(line)):
            trans_lines[i].append(line[i])

# Выводим строки преобразованного текста,
# соединяя элементы каждого подсписка пробелами:
for line in trans_lines:
    print(' '.join(line))
