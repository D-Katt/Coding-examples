# В некотором физическом эксперименте показания прибора снимались
# с частотой 5 измерений в секунду. Эксперимент проводился в течение
# довольно большого времени, и в результате накопилось очень много данных.
# Ученых, которые проводили данный эксперимент, очень интересует,
# какое максимальное значение измеряемой величины достигалось во время измерения.
# Но вот беда: на остановку установки также требуется секунда времени,
# и в течение этого времени с установки могут приходить совершенно любые значения величины.
# В связи с этим, показания последних 5 измерений учитывать при поиске максимального значения не следует.
# Вам необходимо написать программу, которая в данном потоке чисел заранее неизвестной длины
# находит максимальное значение, отбрасывая при этом последние 5 измерений.
# На вход вашей программе передается последовательность натуральных чисел -
# результаты измерений. Каждое новое число передается с новой строки.
# Гарантируется, что длина входной последовательности не меньше 6
# и не превосходит 10 ** 9. На конце последовательности передается число 0.
# Программа должна вывести на экран одно число -
# максимальное значение входной последовательности за исключением последних 5 элементов.

x = int(input())

max_result = x

latest1 = x
latest2 = x
latest3 = x
latest4 = x
latest5 = x

while x != 0:

    if latest1 > max_result:
        max_result = latest1

    latest1 = latest2
    latest2 = latest3
    latest3 = latest4
    latest4 = latest5
    latest5 = x

    x = int(input())

print(max_result)
