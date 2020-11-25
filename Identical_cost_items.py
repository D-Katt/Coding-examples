# Приобретено 72 одинаковых предмета. Стоимость одного предмета является целым числом.
# Общая стоимость покупки составила _679_ (пятизначное число, первая и последняя цифра пропущены).
# Необходимо найти стоимость одного предмета и общую стоимость покупки.

n_items = 72
total_string = '679'

result = False

for first_num in range(1, 10):
    for last_num in range(10):
        total = str(first_num) + total_string + str(last_num)
        if int(total) % n_items == 0:
            result = True
            break
    if result:
        break

if result:
    print(f'Total = {total}')
    print(f'Price = {int(total) // n_items}')
else:
    print('No solution')
