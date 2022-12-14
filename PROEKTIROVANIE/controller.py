import view
import model
import logging

logging.basicConfig(filename='log.txt',
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.INFO, encoding="utf-8")



def main_function():
    try:
        select = view.greeting()
        if select == 1:
            logging.info("выбран 1")
            prime = view.get_math_example()
            result = model.cacl(prime)
            view.view_result(result)
        elif select ==2:
            logging.info("выбран 2")
            massa = view.get_massa()
            logging.info(f"масса стала {massa}")
            value = model.converter(massa)
            view.view_result(value)
            logging.info(f"результат выведен тне энд")
    except Exception as error:
        logging.warning(f"Ну прям совсем жопа, не получилось ничего, {error}")
