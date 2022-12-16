# Задача Измените код одной-двух решенных ранее задач (с прошлых семинаров или домашних работ),
# применив лямбды, filter, map, zip, enumerate, списочные выражения.


# hw4 task3
# Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.
# [1, 2, 2, 3, 4] -> [1, 3, 4]


user_set = [int(i) for i in input('Введите последовательность чисел: ').split()]
sl = {}
res_list = []

for el in user_set:
    sl[f'{el}'] = user_set.count(el)

for key, value in sl.items():
    if value == 1:
        res_list.append(int(key))

print(res_list)



res_lambda = list(filter(lambda x: user_set.count(x) == 1, user_set))
print(res_lambda)