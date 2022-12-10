# 1
# Напишите программу для построения горизонтальных столбчатых диаграмм с
# помощью символа звёздочки.
# Ввод
# Вывод
# 3 7 1 10 8
# ***
# *******
# *
# **********
# ********

# num = input("Ведите числа через пробел: ").split()
# for i in range(len(num)):
#     print("*"* int(num[i]))

# 2
# На первой строке вводится натуральное число N — количество строк.
# Далее следуют N строк, которые надо будет отсортировать
# Ввод
# Вывод
# 4
# три
# три
# пять
# четыре
# шесть
# пять
# четыре
# шесть
# string = []
# num = int(input("введите натуральное число: "))
# for i in range(num):
#     st = input(f"Введите {i+1} строку")
#     string.append(st)
# string.sort(key=lambda x: len(x))
# print(*string, sep="\n")


# 3
# Дан список чисел. Вывести из него только простые числа.
# Ввод
# Вывод
# 15 2 3 31
# 2 3 31

num = [15, 2, 3, 31]
def opredelenie(n):
    count = 0
    for i in range(2, n//2+1):
        if n % i == 0:
            count +=1
    if count > 1:
        return False
    return True
result = list(filter(opredelenie, num))
print(result)
