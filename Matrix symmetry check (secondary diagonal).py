# Проверьте, является ли двумерный массив симметричным относительно побочной диагонали.
# Побочная диагональ — та, которая идёт из правого верхнего угла двумерного массива в левый нижний.
# Программа получает на вход число n <= 100, являющееся числом строк и столбцов в массиве.
# Далее во входном потоке идет n строк по n чисел, являющихся элементами массива.
# Программа должна выводить слово yes для симметричного массива и слово no для несимметричного.

n = int(input("Введите размер массива (n строк по n чисел): "))

a = [0] * n

print("Введите массив построчно, отделяя значения внутри ряда пробелами: ")
for i in range(n):
    a[i] = [int(s) for s in input().split()]

for i in range(n):
    for j in range(-1, -n - 1, -1):
        if a[i][j] != a[-j-1][-i-1]:
            print("no")
            exit()

print("yes")
