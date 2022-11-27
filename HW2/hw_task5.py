# Реализуйте алгоритм перемешивания списка(shuffle использовать нельзя,
# другие методы из библиотеки random - можно).
import random
sp =[1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
print("Начальный список: ", sp)
for i in range(len(sp)):
    k = random.randint(0, len(sp)-1)
    z = random.randint(0, len(sp)-1)
    sp[k], sp[z] = sp[z], sp[k]
print("Перемешанный список: ", sp)