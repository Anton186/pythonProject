# Иф
# a = 0
# if a > 0:
#     print("Число положительное")
# elif a < 0:
#     print("Число отрицательное")
# else:
#     print("Число", a,"равно нулю")
# for i in range(5):
#     print("Алибаба")
# Цилк вайл
# i = 0
# while i < 5:
#     print("Бубаба")
#     i +=1
# Деление
# n = 587
# print(n // 10) #58
# print(n % 10) #7
# Списки
# sp = list ()
# sp = []
# sp.append(5)
# sp.append(8)
# print(sp)
# Списки
# sp = [1, 5, 3, 89, 22]
# print(sp[0])
# print(sp[1])
# print(sp[-1])
#цикл фор
# for i in range(0, len(sp)):
#     print(sp[i], end=" ") # в одну строку
# print()
# for el in sp:
#     print(el, end=" ") # в одну строку но подругому
# print()
# print(*sp) #быстр способ в одну строку


#на вход N и выводит числа от -н до н
# number_n = int(input("введите число"))
# for i in range(-number_n, number_n+1):
#     print(i,end=" ")
#
# на вход дробь


# x, y = [int(i) for i in input().split()] # ввести 2 числа и считать как числа

#словарь наполнить
# slovar = {}
# slovar["city"] = "Moscow"
# print(slovar)

# # Обращение к словарю
# access = {'login': 'ivan', 'password': '123'}
# login = input('Введите логин ')
# password = input('Введите пароль ')
# if login == access['login'] and password == access['password']:
#     print('Вход разрешен')


# sp = [1, 1, 1, 4, 2, 5, 5, 5, 4]
# slov = {}
# for el in sp:
#     if el not in slov:
#         slov[el] = 1
#     else:
#         slov[el] +=1
# print(slov)
# print(slov.get(2, "жопа")) #ищет 2, пишет сколько раз встретилось 2, если нет пишет жопа

# sp = [8, 11, 0, -23, 140, 1]
# res = list(filter(lambda x:10 < abs(x)<100, sp))
# print(res)

# sp = ["1", "a", "b", "2", "3", "c"]
# a = list(filter(lambda x: x.isdigit(),sp))
# print(a)
# b = list(filter(lambda x: x.isalpha(),sp))
# print(b)

# Предположим, вы переписываете у друга рецепты в блокнотик, но вам не нравится лук. Переписывайте без него.
#
# Формат ввода
# На первой строке вводится натуральное число N — количество пунктов рецепта.
# Далее следуют N строк — пункты рецепта.
#
# Формат вывода
# Одна строка — пункты рецепта, разделённые запятой и пробелом, без пунктов с упоминанием лука
# (то есть таких, в которых нет подстроки "лук" в нижнем регистре).
# 5
# лук 1 головка
# картофелин штук 6
# картошку почистить
# лук порезать кольцами
# зажарить всё

# n= 5
# sp=[]
# for i in range(5):
#     sp.append(input())
# print(sp)
# sp = list(filter(lambda x: "лук" not in x, sp))
# sp.sort(key = lambda x: len(x))
# print(*sp,sep=", ")
# print(", ".join(sp))

# sp = ['a', 'b', 'c'] #нумерация списка и вывод его
# for i, el in enumerate(sp, 1):
#     print(i, el)
# sp = [1, 2, 3, 8, 55, 38]
# def f(x):
#     return x**3
# list = [f(i) for i in range(1, sp) if i %2 ==0]
# print(list)

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
#
# num = [15, 2, 3, 31]
# def opredelenie(n):
#     count = 0
#     for i in range(2, n//2+1):
#         if n % i == 0:
#             count +=1
#     if count > 1:
#         return False
#     return True
# result = list(filter(opredelenie, num))
# print(result)