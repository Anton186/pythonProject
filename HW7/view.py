def show_type():
    print("Выберите формат для сохранения:\nВыберите 1 для формата .scv\nВыберите 2 для формата .txt")
    try:
        select = int(input())
        if not select in [1, 2]:
            raise ValueError
        return select
    except Exception:
        print("Выбран не верный формат")
        exit()


def show_menu():
    print("Выберите команду :\n1 - показать весь справочник\n"
          "2 - добавить запись\n3 - изменить запись\n4 - удалить запись")
    try:
        select = int(input())
        if not select in [1, 2, 3, 4]:
            raise ValueError
        return select
    except Exception:
        print("Всё пропало!!!")
        exit()


def show_employees(spisok):
    print("Список всего справочника :")
    for i, sotrudnik in enumerate(spisok):
        if i == 0:
            print(" ", *sotrudnik)
        else:
            print(i, *sotrudnik)


def show_employees_txt(spisok):
    print("Список всего справочника :")
    for i, sotrudnik in enumerate(spisok):
            print(sotrudnik)


def add_employees():
    print("Введите Фамилию Имя Телефон и Описание через пробел: ")
    data = input().split()
    return data


def change_employees():
    print("Выберите строку для перезаписи: ")
    change = int(input())
    print("Введите строку для записи: ")
    string = input().split()
    return change, string


def delete():
    print("Напишите номер записи для удаления: ")
    number = int(input())
    return number
