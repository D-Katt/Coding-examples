import math

# Задача: Колода карт
# Из хорошо перетасованной малой колоды карт (от семерок до тузов, 4 масти, всего 32 карты) вам выдают 6 карт подряд.
# С какой вероятностью выданные карты в сумме дают 50 очков? Считайте, что валет - это 11 очков, дама - 12 очков,
# король - 13 очков, туз - 14 очков. Число очков для остальных карт совпадает с их номиналом.
# Ответ округлите до шестого знака после точки.

# Формат вывода
# Число от 0 до 1 с шестью знаками после точки. Пример формата ответа: 0.123456

cards = [7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 11, 11, 11, 11,
         12, 12, 12, 12, 13, 13, 13, 13, 14, 14, 14, 14]

# Количество способов выбрать 6 карт из колоды в 32 карты:
n_cards = 32
selected_cards = 6

all_combinations = math.factorial(n_cards) / (math.factorial(selected_cards)
                                              * math.factorial(n_cards - selected_cards))

# Всего комбинаций из 6-ти карт: 906192

target_combinations = 0

for first in range(n_cards):
    for second in range(first + 1, n_cards):
        for third in range(second + 1, n_cards):
            for forth in range(third + 1, n_cards):
                for fifth in range(forth + 1, n_cards):
                    for sixth in range(fifth + 1, n_cards):
                        if cards[first] + cards[second] + cards[third] + cards[forth]\
                                + cards[fifth] + cards[sixth] == 50:
                            target_combinations += 1

# Комбинаций по 50 очков: 2698

probability = target_combinations / all_combinations

print(round(probability, 6))

# Вероятность: 0.002977
