# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#
# Пример:
#
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
from typing import List, Any

n = int(input("Введите число:"))
sum = 1
lt = []
for i in range(1, n+1):
    lt.append(sum * i)
    sum = sum * i
print(lt)