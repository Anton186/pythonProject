import view
import models
import logging

# logging.basicConfig(filename='log.txt',
#                     filemode='a',
#                     format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
#                     datefmt='%H:%M:%S',
#                     level=logging.DEBUG, encoding="UTF-8")


def main():
    select = view.show_type()
    if select == 1:
        select = view.show_menu()
        if select == 1:
            sotr = models.get_lists_csv()
            view.show_employees(sotr)
        elif select == 2:
            data = view.add_employees()
            models.add_employees_to_list_csv(data)
        elif select == 3:
            change, string = view.change_employees()
            print(change, string)
            models.update_employees_csv(change, string)
        elif select == 4:
            number = view.delete()
            models.delete_csv(number)
        else:
            print("Всё пропало!")
    elif select ==2:
        select = view.show_menu()
        if select == 1:
            sotr = models.get_lists_txt()
            view.show_employees_txt(sotr)
