# Витя хочет придумать новую игру с числами. В этой игре
# от игроков требуется преобразовывать четырехзначные числа
# не содержащие нулей при помощи следующего разрешенного набора действий:
# 1) Можно увеличить первую цифру числа на 1, если она не равна 9.
# 2) Можно уменьшить последнюю цифру на 1, если она не равна 1.
# 3) Можно циклически сдвинуть все цифры на одну вправо.
# 4) Можно циклически сдвинуть все цифры на одну влево.
# Например, применяя эти правила к числу 1234
# можно получить числа 2234, 1233, 4123 и 2341 соответственно.
# Точные правила игры Витя пока не придумал, но пока его интересует вопрос,
# как получить из одного числа другое за минимальное количество операций.
# Во входном файле содержится два различных четырехзначных числа,
# каждое из которых не содержит нулей.
# Программа должна вывести последовательность четырехзначных чисел,
# не содержащих нулей. Последовательность должна начинаться
# первым из данных чисел и заканчиваться вторым из данных чисел,
# каждое последующее число в последовательности должно быть получено
# из предыдущего числа применением одного из правил.
# Количество чисел в последовательности должно быть минимально возможным.

from collections import deque, defaultdict

first_number = int(input())
last_number = int(input())

previous = defaultdict(set)  # Словарь предшествующих чисел для каждого числа-ключа.
# У одного числа может быть несколько потенциальных предшественников.
previous[first_number] = set()  # У первого числа нет предшественников.

distances = {first_number: 0}  # Словарь расстояний от первого числа до каждого последующего.

modifications = deque([first_number])  # Очередь полученных чисел.

while last_number not in distances:
    # Пока искомое число не появится в словаре расстояний,
    cur_number = modifications.popleft()  # берем из очереди 1-й элемент
    # и трансформируем его:

    if cur_number // 1000 != 9:
        next_number = cur_number + 1000
        previous[next_number].add(cur_number)
        if next_number not in distances:  # Если полученное число
            # еще не представлено в словаре distances,
            # добавляем его в словарь и в очередь.
            distances[next_number] = distances[cur_number] + 1
            # Расстояние до нового числа будет на 1 больше
            # расстояния до его предшественника.
            modifications.append(next_number)

    if cur_number % 10 != 1:
        next_number = cur_number - 1
        previous[next_number].add(cur_number)
        if next_number not in distances:
            distances[next_number] = distances[cur_number] + 1
            modifications.append(next_number)

    next_number = int(str(cur_number)[1:] + str(cur_number)[0])
    previous[next_number].add(cur_number)
    if next_number not in distances:
        distances[next_number] = distances[cur_number] + 1
        modifications.append(next_number)

    next_number = int(str(cur_number)[-1] + str(cur_number)[:3])
    previous[next_number].add(cur_number)
    if next_number not in distances:
        distances[next_number] = distances[cur_number] + 1
        modifications.append(next_number)

path = [last_number]  # Список содержит путь первого числа до последнего в обратной последовательности.

cur_number = last_number

# Перебираем предшественников в словаре previous до тех пор,
# пока не встретится первое заданное число.
while cur_number != first_number:
    for number in previous[cur_number]:  # Среди предшественников каждого числа
        # ищем такое, которое на 1 дальше текущего числа.
        if distances[cur_number] - distances[number] == 1:
            path.append(number)
            cur_number = number

for i in range(len(path) - 1, -1, -1):  # Выводим путь в обратной последовательности.
    print(path[i])
