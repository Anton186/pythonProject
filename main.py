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