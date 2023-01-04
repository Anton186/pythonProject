def show_menu():
    print("Выберите команду :\n1 - показать весь справочник\n"
          "2 - добавить запись\n3 - изменить запись\n4 - удалить запись\n5 - экспортировать справочник\n6 - импортировать справочник")
    try:
        select = int(input())
        if not select in [1, 2, 3, 4, 5, 6]:
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


def export_employees():
    print("\nВведите номера сотрудников для экспорта в другой файл через пробел: ", end='')
    numbers = [int(n) for n in input().split()]
    print(numbers)
    return numbers



def expotr(exp, not_exp):
    if len(exp) != 0:
        exp = [str(i) for i in exp]
        print(f"Выполнен экспорт сотрудников с номерами записей: {', '.join(exp)} успешно.")
    else:
        print("Экспорт не осуществлён - не были переданы номера строк присутствующие в базе.")
    if len(not_exp) != 0:
        not_exp = [str(i) for i in not_exp]
        print(f"Такие номера: {', '.join(not_exp)} в базе отсутствуют.")


def imports(imp, not_imp):
    print(f"\nИз файла добавлено в базу записей: {imp}.")
    print(f"Не добавлено записей в базу: {not_imp} - они уже присутствуют в базе.")


def res_expotr(exp, not_exp):
    if len(exp) != 0:
        exp = [str(i) for i in exp]
        print(f"Выполнен экспорт сотрудников с номерами записей: {', '.join(exp)} успешно.")
    else:
        print("Экспорт не осуществлён - не были переданы номера строк присутствующие в базе.")
    if len(not_exp) != 0:
        not_exp = [str(i) for i in not_exp]
        print(f"Такие номера: {', '.join(not_exp)} в базе отсутствуют.")


def res_import(imp, not_imp):
    print(f"\nИз файла добавлено в базу записей: {imp}.")
    print(f"Не добавлено записей в базу: {not_imp} - они уже присутствуют в базе.")
