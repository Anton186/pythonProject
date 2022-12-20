import csv
import logging


def get_lists():
    with open('file1.csv', encoding="utf8") as csvfile:
        reader = csv.reader(csvfile, delimiter=';', )
        #title = next(reader)
        logging.info("что нибудь")
        return list(reader)


def add_employees_to_list(employees):
    with open('file1.csv', 'a', encoding="utf8", newline='', ) as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow(employees)


def update_employees(number, string):
    try:
        with open('file1.csv', 'r', encoding="utf8", newline='', ) as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            data = list(reader)
            data[number] = string
        with open('file1.csv', 'w', encoding="utf8", newline='', ) as csvfile:
            writer = csv.writer(csvfile, delimiter=';')
            for i in data:
                writer.writerow(i)
    except IndexError:
        print("Вы вышли за границы массива")
        exit()
    except Exception:
        print("Появились какие та другие ошибки =(")
        exit()


def delete(number):
    with open('file1.csv', 'r', encoding="utf8", newline='', ) as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        data = list(reader)
        del data[number]
    with open('file1.csv', 'w', encoding="utf8", newline='', ) as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        for i in data:
            writer.writerow(i)
