# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
#
# Пример:
#
# - 6 -> да
# - 7 -> да
# - 1 -> нет


n = int(input("Введите число: "))
if n > 0 and n < 8:
    if n > 5:
        print("Это выходной день!")
    else:
        print("Это будний день")
else:
    print("Это не является днём недели")