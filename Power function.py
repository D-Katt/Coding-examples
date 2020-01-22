# Implement pow(x, n), which calculates x raised to the power n (xn).
# Example 1:
# Input: 2.00000, 10
# Output: 1024.00000
# Example 2:
# Input: 2.10000, 3
# Output: 9.26100
# Example 3:
# Input: 2.00000, -2
# Output: 0.25000
# Explanation: 2-2 = 1/22 = 1/4 = 0.25
# Note:
# -100.0 < x < 100.0
# n is a 32-bit signed integer, within the range [−231, 231 − 1]


def power(x: float, n: int):
    """Функция возвращает результат возведения числа x в степень n."""
    if n == 0:
        result = 1
    else:  # Если n не равен нулю, вычисляем положительную степень числа x,
        # умножая 1 на x циклом for n раз.
        result = 1
        for i in range(abs(n)):
            result *= x

    # Если степень отрицательная, преобразуем полученный результат
    # путем деления единицы на полученное число.
    if n < 0:
        result = 1 / result

    return result


number, p = input().split()

print(power(float(number), int(p)))
