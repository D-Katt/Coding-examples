# Задача: Самый короткий палиндром в строке

# Аркадий — большой фанат использования машинного обучения в любой задаче.
# Он верит в безграничную силу волшебства этой популярной молодой науки.
# Именно поэтому Аркадий постоянно постоянно придумывает всё новые и новые факторы,
# которые можно вычислить для различных объектов.
# Напомним, палиндромом называется строка, которая одинаково читается от начала к концу
# и от конца к началу. Для каждой строки в своей базе данных Аркадий хочет найти
# самую короткую её подстроку, состоящую хотя бы из двух символов и являющуюся палиндромом.
# Если таких подстрок несколько, Аркадий хочет выбрать лексикографически минимальную.

# Формат ввода
# В единственной строке входных данных записана одна строка из базы Аркадия —
# непустая последовательность строчных букв английского алфавита.
# Длина строки составляет не менее 2 и не превосходит 200 000 символов.

# Формат вывода
# Выведите минимальную по длине подстроку строки из входных данных,
# состоящую хотя бы из двух символов и являющуюся палиндромом.
# Напомним, что среди всех таких строк Аркадий хочет найти лексикографически минимальную.

# Пример 1
# Ввод
# abac
# Вывод
# aba

# Пример 2
# Ввод
# yandex
# Вывод
# -1

# Примечания
# Говорят, что строка
# a = a1a2...an лексикографически меньше строки b = b1b2...bm, если верно одно из двух условий:
# - либо n < m и a1 = b1, a2 = b2 ... an = bn, то есть первая строка является префиксом второй;
# - либо есть такая позиция 1 ≤ i ≤ min(n, m), что a1 = b1, a2 = b2 ... ai = bi − 1
#   и ai < bi, то есть, в первой позиции, в которой строки различаются, в первой строке стоит меньшая буква.

string = input()
n_letters = len(string)


def palindrome(s):
    end = len(s)
    middle = end // 2
    for i in range(middle):
        if s[i] != s[end - 1 - i]:
            return False
    return True


iterations = n_letters + 1
step = 1

# Рассматриваем только 2 случая - сегменты из 2 и 3 букв.
for i in range(2):

    step += 1
    substrings = set()

    for start in range(iterations - step):
        # Вычленяем подстроку с шагом step, начиная от стартовой позиции.
        substring = string[start:start + step]

        # Проверяем, является ли подстрока палиндромом.
        if palindrome(substring):
            substrings.add(substring)

        # Если нет - то смещаем стартовую позицию на 1.
        start += 1

    # Если в списке есть элементы, прерываем цикл:
    if substrings:
        break

# В зависимости от длины множества:
if len(substrings) == 0:
    print(-1)  # Нет палиндромов
else:
    print(sorted(substrings)[0])  # 1-й в отсортированной очереди