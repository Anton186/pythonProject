# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
n = int(input("Введите число: "))
sp = []
for i in range(-n, n+1):
    sp.append(i)
f = open("file.txt")
lt=(f.readlines())
lt=[int(x) for x in lt]
sum = 1
for i in range(len(lt)):
    sum = sum * sp[lt[i]]
print(sum)