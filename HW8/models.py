import csv
import logging


def get_lists():
    with open('spravochnik.csv', encoding="utf8") as csvfile:
        reader = csv.reader(csvfile, delimiter=';', )
        # title = next(reader)
        return list(reader)



def add_employees_to_list(employees):
    with open('spravochnik.csv', 'a', encoding="utf8", newline='', ) as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow(employees)


def update_employees(number, string):
    try:
        with open('spravochnik.csv', 'r', encoding="utf8", newline='', ) as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            data = list(reader)
            data[number] = string
        with open('spravochnik.csv', 'w', encoding="utf8", newline='', ) as csvfile:
            writer = csv.writer(csvfile, delimiter=';')
            for i in data:
                writer.writerow(i)
    except IndexError:
        print("Вы вышли за границы массива")
        exit()
    except Exception:
        print("Появились какие-то другие ошибки =(")
        exit()


def delete(number):
    with open('spravochnik.csv', 'r', encoding="utf8", newline='', ) as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        data = list(reader)
        del data[number]
    with open('spravochnik.csv', 'w', encoding="utf8", newline='', ) as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        for i in data:
            writer.writerow(i)


def export_employees_file(numbers):
    exp = []
    exp_i = []
    with open('export.csv', 'r', encoding="utf-8", newline='') as r_file:
        reader = csv.reader(r_file, delimiter=';')
        data = list(reader)
        for i, sotrudnik in enumerate(data):
            if i in numbers:
                exp.append(sotrudnik)
                exp_i.append(i)
                numbers.remove(i)
    with open('export.csv', 'w', encoding="utf-8", newline='') as w_file:
        writer = csv.writer(w_file, delimiter=';')
        writer.writerow(["Имя", "Фамилия", "Телефон", "Должность"])
        for i in exp:
            writer.writerow(i)
    return exp_i


def import_exployees_file():
    with open('import.csv', 'r', encoding="utf-8", newline='') as r_file:
        reader1 = csv.reader(r_file, delimiter=';')
        data1 = list(reader1)
        data1.pop(0)
        d = len(data1)
        count = 0
    with open('spravochnik.csv', 'r', encoding="utf-8", newline='') as r_file:
        reader2 = csv.reader(r_file, delimiter=';')
        data2 = list(reader2)
    with open('spravochnik.csv', 'a', encoding="utf-8", newline='') as a_file:
        writer = csv.writer(a_file, delimiter=';')
        for s in data1:
            if s not in data2:
                writer.writerow(s)
                count += 1
    return str(count), str(d - count)


def create(fl):
    with open(fl, 'w', encoding="utf-8", newline='') as w_file:
        writer = csv.writer(w_file, delimiter=';')
        writer.writerow(["Имя", "Фамилия", "Телефон", "Должность"])