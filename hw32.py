from datetime import datetime



# def make_rounder(digits):
#     def round_number(x):
#         return round(x, digits)
#     return round_number
#
# round2 = make_rounder(2)
# round0 = make_rounder(1)
#
#
# print(round2(3.14159))
# print(round2(2.71828))
# print(round0(9.999))


# def make_logger():
#     events = []
#     def log(message=None):
#         if message:
#             current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#             events.append(f"{message}: {current_time}")
#         return events
#     return log
#
# log = make_logger()
# log("Загрузка данных")
# log("Обработка завершена")
# log("Сохранение файла")
#
# for event in log():
#     print(event)


def frame(func):
    def wrapper(*args, **kwargs):
        print("-" * 50)
        result = func(*args, **kwargs)
        print("-" * 50)
        return result
    return wrapper

@frame
def hello_world():
    print("Hello World!")

hello_world()