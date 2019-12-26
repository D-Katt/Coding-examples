# По заданной дате требуется определить, какое число будет послезавтра.
# Напомним, что год является високосным, если его номер кратен 4,
# но не кратен 100, а также если он кратен 400.
# Дано число, месяц и год (год  – число в промежутке от 1 до 10000).
# Требуется вывести, какое число будет послезавтра, в формате входных данных.

print("Введите день, месяц и год в одну строку через пробел:")

day, month, year = (int(s) for s in input().split())

Calendar = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
days_per_year = 365

# Проверяем год на високосность и вносим поправки в календарь.
if year % 4 == 0 and year % 100 != 0:
    Calendar[2] = 29
    days_per_year = 366
elif year % 400 == 0:
    Calendar[2] == 29
    days_per_year = 366

# Подсчитываем, какой день идет с начала года, и прибавляем 2 дня.
count = 0

for i in range(1, month):
    count += Calendar[i]

count += (day + 2)

# Если мы превысили количество дней в текущем году и оказались в январе следующего:
if count > days_per_year:
    count -= days_per_year
    year += 1

total = 0

for i in range(1, 13):
    pr = total
    month = i
    day = count - pr
    total += Calendar[i]
    if total >= count:
        break

print("Day:", day, "Month:", month, "Year:", year)