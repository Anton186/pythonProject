import csv
import logging


def get_lists_csv():
    with open('spravochnik.csv', encoding="utf8") as csvfile:
        reader = csv.reader(csvfile, delimiter=';', )
        #title = next(reader)
        logging.info("что нибудь")
        return list(reader)


def get_lists_txt():
    with open('spravochnik.txt', encoding="utf8") as txtfile:
        reader = txtfile.readlines()
        #title = next(reader)
        return list(reader)



def add_employees_to_list_csv(employees):
    with open('spravochnik.csv', 'a', encoding="utf8", newline='', ) as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow(employees)

def add_employees_to_list_txt(employees):
    with open('spravochnik.txt', 'a', encoding="utf8", newline='\n', ) as txtfile:
        for i in range(len(employees)):
            txtfile.write(f"{(employees[i])}\n")




def update_employees_csv(number, string):
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
        print("Появились какие та другие ошибки =(")
        exit()


def delete_csv(number):
    with open('spravochnik.csv', 'r', encoding="utf8", newline='', ) as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        data = list(reader)
        del data[number]
    with open('spravochnik.csv', 'w', encoding="utf8", newline='', ) as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        for i in data:
            writer.writerow(i)
