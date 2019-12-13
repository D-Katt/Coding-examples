# Кузнечик-брокер
# Кузнечик находится на Бирже, которая является числовой прямой,
# в клетке №1 и собирается заработать денег. В каждой клетке числовой прямой,
# которую он посещает, он вынужден заключить сделку со всеми имеющимися средствами.
# При этом он может получить как прибыль, так и убыток.
# Прибыльность каждой клетки задана процентами со знаком.
# Если знак положительный — сделка увеличивает сумму денег Кузнечика
# на указанный процент от его текущей суммы. Если отрицательный —
# сделка уменьшает сумму денег Кузнечика на указанный процент.
# В самой клетке №1 никакой сделки не заключается.
# Вывести на экран путь, максимизирующий сумму, которую сможет заработать
# Кузнечик на бирже, если он может совершать прыжки на клетку с номером +2 и +3 от текущей,
# но не может прыгнуть на соседнюю клетку.
# Обратите внимание, что Кузнечик не обязан останавливаться в точке
# последней возможной сделки! Более того, если совершение сделок окажется убыточным,
# Кузнечик имеет право остаться в клетке №1 с исходным капиталом.
# Формат входных данных
# В первой строке записано целое число — стартовый капитал Кузнечика.
# Во второй строке записаны целые числа — проценты со знаком + или -.
# Доходность не превышает 1000%, а убыточность -100%.
# Отрицательный баланс у Кузнечика недопустим.
# Максимальный номер клетки задаётся количеством чисел в строке ввода.
# Формат выходных данных
# Клетки, по которым должен пройти Кузнечик, чтобы получить максимальную выгоду.

from collections import deque

capital = int(input())
profitability = [int(s) for s in input().split()]


def max_profit(n: int, l: list):
    """Функция принимает два аргумента:
    n - размер стартового капитала, l - список доходности каждой клетки.
    Возвращает путь максимальной доходности для кузнечика
    с допустимыми прыжками +2 и +3."""
    e = len(l)
    C = [(n, 0), (-1, -1), ((1 + l[2] / 100) * n, 0), ((1 + l[3] / 100) * n, 0)]
    # Список С хранит значения максимально возможной величины капитала (C[i][0])
    # и индексы клеток-предшественников (C[i][1]) для каждой клетки пути.
    # В первой клетке стартовый капитал. Вторая клетка недопустима для прыжка.
    # Клетки 3 и 4 рассчитываются по значениям доходности.

    if C[0][0] > C[2][0] and C[0][0] > C[3][0]:
        end_point = C[0][0]  # В переменной end_point будет храниться максимальная величина капитала.
        ind = 0  # В переменной ind будет храниться индекс элемента списка С с макс. капиталом.
    else:
        if C[2][0] > C[3][0]:
            end_point = C[2][0]
            ind = 2
        else:
            end_point = C[3][0]
            ind = 3

    if e > 4:
        for i in range(4, e):
            if C[i-3][0] > C[i-2][0]:
                C.append(((1 + l[i] / 100) * C[i-3][0], i - 3))
            else:
                C.append(((1 + l[i] / 100) * C[i-2][0], i - 2))
            # Перебираем оставшиеся доходности списка l
            # и для кадой новой клетки добавляем в список С кортеж из двух элементов:
            # максимально достижимая в этой клетке величина капитала и индекс предшественника.

            if C[i][0] > end_point:  # При достижении нового максимума обновляем значения ind и end_point.
                ind = i
                end_point = C[i][0]

    way = deque([ind + 1])  # Сохраняем его в список way, увеличив на 1 для соответствия порядковому номеру клетки.

    while ind > 0:  # Перебираем значения списка C от индекса клетки с макс. капиталом к нулю.
        ind = C[ind][1]  # Находим индекс клетки-предшественника и обновляем ind.
        way.appendleft(ind + 1)  # Добавляем его в начало списка way.

    return way


res = max_profit(capital, profitability)

for el in res:
    print(el, end=" ")