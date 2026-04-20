from random import choice
import random
import time



# def new_range(start, stop, step):
#     if step > 0:
#         while start < stop:
#             yield start
#             start += step
#     else:
#         while start > stop:
#             yield start
#             start += step
#
# for i in new_range(20,10,-2):
#     print(i)


# def new_range1(start, stop, step):
#     yield from range(start, stop, step)
#
# for i in new_range1(20,10,-2):
#     print(i)

'''2. Генератор случайных дат
Создайте генератор, который генерирует случайные даты в пределах одного года.
Генератор должен принимать год в качестве аргумента и выдавать следующую
случайную дату при каждом вызове, учитывая количество дней в месяце, а также
високосные годы.
'''


#
# def is_leap(year: int) -> bool:
#     """
#     Return boolean if year is leap year
#     :param year: year
#     :return: boolean
#     """
#     return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
#
# def day_generate(year):
#     days = {1:31,2:29 if is_leap(year) else 28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
#     while True:
#         month = random.randint(1,12)
#         day = random.randint(1,days[month])
#         yield (year, month, day)
#
# years = day_generate(2020)





'''Создайте генератор, который выдаёт случайные имена и фамилии.
Выведите 5 имён.
Для получения случайного значения из списка можно использовать choice() из
модуля random.'''





# first_names = ["Alice", "Bob", "Charlie", "David", "Emma"]
# last_names = ["Smith", "Johnson", "Brown", "Williams", "Jones"]
#
# def random_names(first_names, last_names):
#     while True:
#         first = random.choice(first_names)
#         last = random.choice(last_names)
#         yield first, last
#
#
# names = random_names(first_names, last_names)




'''4. Генератор тестовых данных
Создайте генератор, который принимает список других генераторов и возвращает
кортежи, состоящие из значений, полученных от каждого из них.
Используйте ранее написанные генераторы дат и имён для создания тестовых
данных.'''

# name_gen = random_names(first_names, last_names)
# date_gen = day_generate(2025)
#
# def tuple_of_generators(*generators):
#     while True:
#         yield tuple(next(gen) for gen in generators)
#
#
# combi_gen = tuple_of_generators(name_gen, date_gen)
#
# for _ in range(5):
#     print(next(combi_gen))


with open("tasks.txt", "w", encoding="utf=8") as file:
    while True:
        task = input('Write task or EXIT for exit: ')
        if task.lower() == 'exit':
            break
        file.write(f"{task}\n")




'''Эта программа читает файл tasks.txt и назначает задачи сотрудникам по
очереди.
Она использует генератор для постепенного чтения новых задач и назначения
сотрудникам.
Дополнительно: если файл tasks.txt отсутствует, программа делает 5 попыток с
паузой 3 секунды перед завершением.
'''

employees = ["Alice", "Bob", "Charlie"]




