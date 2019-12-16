# Мальчику Васе очень нравится известная игра "Сапер" ("Minesweeper"). В "Сапер" играет один человек.
# Игра идет на клетчатом поле (далее будем называть его картой) NxM (N строк, M столбцов).
# В K клетках поля стоят мины, в остальных клетках записано либо число от 1 до 8 — количество мин в соседних клетках,
# либо ничего не написано, если в соседних клетках мин нет.
# Клетки являются соседними, если они имеют хотя бы одну общую точку, в одной клетке не может стоять более одной мины.
# Изначально все клетки поля закрыты. Игрок за один ход может открыть какую-нибудь клетку.
# Если в открытой им клетке оказывается мина — он проигрывает, иначе игроку показывается число,
# которое стоит в этой клетке, и игра продолжается. Цель игры — открыть все клетки, в которых нет мин.
# У Васи на компьютере есть эта игра, но ему кажется, что все карты, которые в ней есть, некрасивые и неинтересные.
# Поэтому он решил нарисовать свои. Однако фантазия у него богатая, а времени мало, и он хочет успеть нарисовать
# как можно больше карт. Поэтому он просто выбирает N, M и K и расставляет мины на поле, после чего
# все остальные клетки могут быть однозначно определены. Однако на определение остальных клеток
# он не хочет тратить свое драгоценное время. Помогите ему!
# По заданным N, M, K и координатам мин восстановите полную карту.
# В первой строке входного файла содержатся числа N, M и K (1<=N<=200, 1<=M<=200, 0<=K<=N x M).
# Далее идут K строк, в каждой из которых содержится по два числа, задающих координаты мин.
# Первое число в каждой строке задает номер строки клетки, где находится мина, второе число — номер столбца.
# Левая верхняя клетка поля имеет координаты (1,1), правая нижняя — координаты (N,M).
# Выходной файл должен содержать N строк по M символов — соответствующие строки карты. j-й символ
# i-й строки должен содержать символ ‘*‘ (звездочка) если в клетке (i,j) стоит мина, цифру от 1 до 8,
# если в этой клетке стоит соответствующее число, либо ‘.‘ (точка), если клетка (i,j) пустая.

print("Введите через пробел длину и ширину поля, количество мин:")
N, M, K = (int(s) for s in input().split())

# Создаем массив точек, превышающий размеры поля на 1 единицу с каждой стороны.
A = [['.'] * (M+2) for s in range(N+2)]

# Создаем 2 пустых списка координат мин.
mines_N = [0] * K
mines_M = [0] * K

print("Введите координаты мин (по 2 числа через пробел, каждая новая позиция - с новой строки):")
for i in range(K):
    mines_N[i], mines_M[i] = (int(s) for s in input().split())

# Расставляем мины на поле в соответствии с введенными координатами.
for i in range(K):
    A[mines_N[i]][mines_M[i]] = '*'

# Подсчитываем количество мин в соседних с пустыми клетках:
for i in range(1, N + 1):
    for j in range(1, M + 1):
        c = 0
        if A[i][j] == '.':
            if A[i-1][j] == '*':
                c += 1
            if A[i-1][j+1] == '*':
                c += 1
            if A[i-1][j-1] == '*':
                c += 1
            if A[i][j+1] == '*':
                c += 1
            if A[i][j-1] == '*':
                c += 1
            if A[i+1][j] == '*':
                c += 1
            if A[i+1][j-1] == '*':
                c += 1
            if A[i+1][j+1] == '*':
                c += 1
            if c > 0:
                A[i][j] = c

# Выводим поле с минами и цифрами:
for i in range(1, N + 1):
    for j in range(1, M + 1):
        print(A[i][j], end=' ')
    print()