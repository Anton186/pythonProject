# 1
# Задайте строку из набора чисел. Напишите программу, которая покажет большее и
# меньшее число. В качестве символа-разделителя используйте пробел.
list = [int(i) for i in input("напиши че нибудь а ").split()]
print(max(list))
print(min(list))

list1 = [int(i) for i in input("напиши че нибудь без пробелов ")]
print(max(list1))
print(min(list1))