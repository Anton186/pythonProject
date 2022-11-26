# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

N = int(input("Введите номер четверти: "))
if N == 1:
    print("Возможные варианты X > 0 и Y > 0")
elif N == 2:
    print("Возможные варианты X > 0 и Y < 0")
elif N == 3:
    print("Возможные варианты X < 0 и Y < 0")
elif N == 4:
    print("Возможные варианты X < 0 и Y > 0")
else:
    print("Данное число не является номером четверти")