# Покупая билет в кино, пользователь сервиса может указать свой email или телефон, либо email и телефон сразу.
# Напишите алгоритм, который по списку таких транзакций находит пользователя, купившего больше всех билетов.
# В качестве ответа укажите число строк в исходном файле, которые относятся к этому пользователю.
# Под пользователем понимается email, телефон или комбинация обоих идентификаторов,
# если их удастся связать по логам покупок.

# Пример связывания пользователей по логам:
# user_1@contest.yandex.ru, 880111111111
# user_1@contest.yandex.ru, 880222222222
# user_2@contest.yandex.ru, 880222222222
# user_3@contest.yandex.ru, 880333333333

# В этом примере адреса user_1@contest.yandex.ru, user_2@contest.yandex.ru и телефоны 880111111111,
# 880222222222 относятся к одному пользователю. А user_3@contest.yandex.ru и 880333333333 — к другому.

# Формат ввода
# Логи покупок доступны в файле logs.csv. В первом столбце указан email пользователя, во втором — телефон.

# Формат вывода
# Целое число строк.

import pandas as pd
from collections import defaultdict, deque

data = pd.read_csv('logs.csv', header=None)
data.columns = ['mail', 'phone']

# Убираем пропуски и дубликаты:
unique_data = data.dropna().drop_duplicates()

# Составляем граф по номерам телефонов и мейлам:
graph = defaultdict(list)

for mail, phone in unique_data.values:
    graph[mail].append(phone)
    graph[phone].append(mail)


def identify_user(node):
    """Функция производит обход графа от заданной вершины
    (номер телефона или почтовый адрес) и возвращает список телефонов
    и мейлов, связанных с одним уникальным пользователем."""

    # Очередь обхода:
    nodes = deque([node])

    # Посещенные вершины:
    visited = set()
    visited.add(node)

    # Обход связанных вершин:
    while nodes:
        cur_v = nodes.popleft()
        for neigh_v in graph[cur_v]:
            if neigh_v not in visited:
                visited.add(neigh_v)
                nodes.append(neigh_v)

    return list(visited)


n_transactions = 0

# Пока в данных остаются строки:
while len(data) > 0:
    # Среди номеров телефонов есть пропуски, поэтому берем первый мейл:
    user_mail = data.iloc[0, 0]
    # Находим все связанные с ним номера телефонов и мейлы:
    user_id = identify_user(user_mail)
    # Количество строк, относящихся к текущему пользователю:
    cur_user = data[(data['mail'].isin(user_id)) | (data['phone'].isin(user_id))]
    user_transactions = len(cur_user)
    # Сравниваем с максимумом:
    if user_transactions > n_transactions:
        n_transactions = user_transactions
    # Удаляем из данных все строки, относящиеся к текущему пользователю:
    indexes = cur_user.index
    data = data.drop(indexes)

print('Наибольшее число строк одного пользователя:', n_transactions)

# Наибольшее число строк одного пользователя: 5192
