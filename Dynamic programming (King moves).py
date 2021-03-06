# Двумерное динамическое программирование: игра с королем.
# Рассмотрим игру «Короля в угол» для двух игроков.
# В левом верхнем углу доски размером N*M находится король,
# который может двигаться только вправо-вниз на 1 клетку.
# Игроки по очереди двигают ферзя, то есть за один ход игрок
# может переместить ферзя либо по вертикали вниз на 1 клетку,
# либо по горизонтали вправо, либо во диагонали вправо-вниз на 1 клетку.
# Выигрывает игрок, который поставит ферзя в правый нижний угол.
# Необходимо определить, какой из игроков может выиграть в этой игре
# независимо от ходов другого игрока (имеет выигрышную стратегию).
# Будем заполнять доску знаками «+» и «-». Знак «+» будет означать,
# что данная клетка является выигрышной для ходящего с неё игрока
# (то есть если король стоит в этой клетке, то игрок, который делает ход,
# может всегда выиграть), а знак «-» означает, что он проигрывает.
# В правом нижнем углу необходимо поставить знак «-» — если король стоит в углу,
# то тот игрок, которых должен делать ход, уже проиграл.


def chess_field(width, height):
    """Функция принимает две переменные: ширину и высоту игрового поля.
    Возвращает двумерный массив, в котором "+" обозначены выигрышные клетки и
    "-" обозначены проигрышные клетки."""

    field = [["?" for _ in range(width)] for _ in range(height)]  # создаем двумерный массив

    field[height-1][width-1] = "-"  # правая нижняя клетка проигрышная, т.к. игра уже закончена
    field[height-1][width-2] = field[height-2][width-1] = field[height-2][width-2] = "+"
    # Эти клетки всегда выигрышные.

    for i in range(-1, -height - 1, -1):  # Перебираем элементы массива в обратном порядке от конца каждой
        for j in range(-1, -width - 1, -1):  # строки к ее началу, начиная с предпоследней строки.
            if field[i][j] != "?":  # Если клетка уже заполнена, запускаем следующий цикл.
                continue
            else:  # Если клетка не заполнена,
                if j < -1:
                    if field[i][j+1] == "-":  # и следующая от нее вправо клетка содержит "-", то
                        field[i][j] = "+"  # текущая клетка выигрышная.
                        continue
                if i < -1:
                    if field[i+1][j] == "-":  # если следующая вниз клетка содержит "-", то
                        field[i][j] = "+"  # текущая клетка выигрышная.
                        continue
                if i < -1 and j < -1:
                    if field[i+1][j+1] == "-":  # если следующая по диагонали содержит "-", то
                        field[i][j] = "+"  # текущая клетка выигрышная.
                        continue
            if field[i][j] == "?":  # Если ни один возможных ходов не привел на клетку с "-", то
                field[i][j] = "-"  # текущая позиция проигрышная.
    return field


field = chess_field(8, 8)  # Вызываем функцию для поля 8 х 8 клеток

for row in field:  # Выводим полученный массив
    for position in row:
        print(position, end=" ")
    print()
