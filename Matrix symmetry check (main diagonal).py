# Проверьте, является ли двумерный массив симметричным относительно главной диагонали.
# Главная диагональ — та, которая идёт из левого верхнего угла двумерного массива в правый нижний.
# Программа получает на вход число n <= 100, являющееся числом строк и столбцов в массиве.
# Далее во входном потоке идет n строк по n чисел, являющихся элементами массива.
# Программа должна выводить слово yes для симметричного массива и слово no для несимметричного.

n = int(input("Введите размер массива (n строк по n чисел): "))

A = [0] * n

print("Введите массив построчно, отделяя значения внутри ряда пробелами: ")
for i in range(n):
    A[i] = [int(s) for s in input().split()]

for i in range(n):
    for j in range(n):
        if A[i][j] != A[j][i]:
            print("No")
            exit()

print("Yes")