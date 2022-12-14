def greeting():
    print("Привет епта! Выбери действие: 1 - калькулятор; 2 - конвертер величин")
    select = int(input())
    return select


def get_math_example():
    primer = input("Введите выражение: ")
    return primer


def view_result(result):
    print(f"Вот твой ответ чертила: {result}")


def get_massa():
    massa = input("Введите массу в кг: ")
    return massa
