# Создайте программу для игры с конфетами человек против человека.
#
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
#
# a) Добавьте игру против бота
#
# b) Подумайте как наделить бота ""интеллектом""

import random
konfety = int(input("Введите количество конфет на столе: "))
maxtake = int(input("Введите максимальное количество забранных конфет за ход: "))
igrok = 1#random.randint(1, 2)
print(f"Жеребьёвкой определен первый ход игрока: {igrok}\nКонфет на столе:{konfety}\nМаксимально можно взять конфет за ход:{maxtake}")
while konfety > maxtake:
    if igrok == 1:
        take = int(input("Игрок 1, введите количество конфет: "))
        while not 0 < take < maxtake+1:
            take = int(input(f"Можно взять не менее одной и не более {maxtake} конфет! Введите количество конфет: "))
        else:
            konfety = konfety - take
        print("Конфет осталось:", konfety)
        igrok = 2
    # elif igrok == 2:
    #     take = int(input("Игрок 2, введите количество конфет: "))
    #     while not 0 < take < maxtake+1:
    #          take = int(input(f"Можно взять не менее одной и не более {maxtake} конфет! Введите количество конфет: "))
    #     else:
    #          konfety = konfety - take
    #     print("Конфет осталось:", konfety)
    #     igrok = 1
    else:
        print("ходит комп")
        if konfety <= maxtake:
            print("иф")
            take = konfety
            print("Компьютер выйграл")
        elif konfety % maxtake == 0:
            print("элиф")
            take = maxtake - 1
            igrok = 1
        else:
            print("элс")
            take = (konfety % maxtake)
        konfety = konfety - take
        igrok = 1
        print(f"Компьютер взял {take} конфет\nКонфет осталось {konfety}")

#take = total_count % 29 if total_count % 29 != 0 else random.randint(1, 28)

