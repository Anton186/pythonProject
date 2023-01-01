import view
import models
import logging

# logging.basicConfig(filename='log.txt',
#                     filemode='a',
#                     format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
#                     datefmt='%H:%M:%S',
#                     level=logging.DEBUG, encoding="UTF-8")


def main():
    select = view.show_menu()
    if select == 1:
        sotr = models.get_lists()
        view.show_employees(sotr)
    elif select == 2:
        data = view.add_employees()
        models.add_employees_to_list(data)
    elif select == 3:
        change, string = view.change_employees()
        print(change, string)
        models.update_employees(change, string)
    elif select == 4:
        number = view.delete()
        models.delete(number)
    elif select == 5:
        logging.info("\nВыбрана команда - экспорт выбранных сотрудников в файл.")
        nums = view.export_employees()
        exports = models.export_employees_file(nums)
        logging.warning(f"Выполнен экспорт сотрудников с номерами записей: {exports} в файл.")
        view.res_expotr(exports, nums)
    elif select == 6:
        logging.info("\nВыбрана команда - импорт сотрудников из файла.")
        count1, count2 = models.import_exployees_file()
        logging.warning("Успешный импорт сотрудников из файла.")
        view.res_import(count1, count2)
    else:
        print("Введена неверная команда")