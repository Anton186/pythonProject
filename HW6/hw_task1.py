# Наибольший общий делитель
# В модуле math есть функция math.gcd(a, b), возвращающая наибольший общий делитель (НОД) двух чисел.
# Вычислите и напечатайте наибольший общий делитель для списка натуральных чисел. Ввод чисел продолжается до ввода пустой строки.
# Входные данные Выходные данные
# 36 6
# 12
# 144
# 18
import math

list = []
n = 0
while n != "":
    list.append(int(n))
    n = (input("Введите числа, по окончании оставьте пустую строку: "))
k = math.gcd(*list,)
print(f"Наиюбольшее общее кратное чисел: {k}")
