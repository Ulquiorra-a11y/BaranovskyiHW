import logging


logging.basicConfig(
    filename='app.log',
    format="%(asctime)s - %(filename)s - %(lineno)d - %(levelname)s - %(message)s",
    level=logging.DEBUG
)


def devide_numbers(a: int, b: int) -> float:
    '''
    This function divides two numbers.
    :param a:  number
    :param b:  number
    :return: devided number
    '''
    return a / b


try:
    a = int(input("Введите делимое: "))
    b = int(input("Введите делитель: "))
    print(devide_numbers(a, b))
except ValueError:
    print("Error: Incorrect number entered.")
    logging.error("Error: Incorrect number entered.")
except ZeroDivisionError:
    logging.error("Error: Division by zero is not possible.")
    print("Error: Division by zero is not possible.")