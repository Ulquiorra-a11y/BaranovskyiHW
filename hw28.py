from itertools import cycle
from itertools import chain
from itertools import product
from typing import Any, Generator


'''Напишите программу, которая помогает планировать дела.
Программа должна бесконечно выводить план на следующий день недели, пока пользователь нажимает 'Enter'.'''
# weekly_schedule = {
#     "Monday": ["Gym", "Work", "Read book"],
#     "Tuesday": ["Meeting", "Work", "Study Python"],
#     "Wednesday": ["Shopping", "Work", "Watch movie"],
#     "Thursday": ["Work", "Call parents", "Play guitar"],
#     "Friday": ["Work", "Dinner with friends"],
#     "Saturday": ["Hiking", "Rest"],
#     "Sunday": ["Family time", "Rest"]
# }
#
# days_cycle = cycle(weekly_schedule.items())
#
# for day, tasks in days_cycle:
#     print(f"{day}: {', '.join(tasks)}")
#
#     user_input = input("\nНажмите Enter для получения плана или q для выхода: ")
#
#     if user_input == "q":
#         print("Выход из программы")
#         break



'''Напишите функцию, которая принимает несколько списков с названиями продуктов и возвращает генератор, содержащий все продукты в нижнем регистре.
Выведите содержимое генератора.'''
# fruits = ["Apple", "Banana", "Orange"]
# vegetables = ["Carrot", "Tomato", "Cucumber"]
# dairy = ["Milk", "Cheese", "Yogurt"]
#
# def all_products(*lists: list[str]) -> Generator[Any, Any, None]:
#     '''
#     Returns a generator that yields all products from multiple iterables
#     converted to lowercase
#     :param lists: lists
#     :return:product names in lowercase
#     '''
#     return (item.lower() for item in chain(*lists))
#
# for fruit in all_products(fruits, vegetables, dairy):
#     print(fruit)



'''Напишите функцию, которая принимает списки типов одежды, цветов и размеров, а затем генерирует все возможные комбинации
в формате "Clothe - Color - Size".'''
clothes = ["T-shirt", "Jeans", "Jacket"]
colors = ["Red", "Blue", "Black"]
sizes = ["S", "M", "L"]


def type_of_clothes(clothes: list[str],colors: list[str],sizes: list[str])-> Generator[str, None, None]:
    '''
    Generates all possible combinations of clothes, colors, and sizes
    :param clothes: list of clothes
    :param colors: list of colors
    :param sizes: list of sizes
    :return: all possible combinations of clothes, colors, and sizes
    '''
    return (f"{cloth} - {color} - {size}"for cloth, color, size in product(clothes, colors, sizes))

for item in type_of_clothes(clothes, colors, sizes):
    print(item)