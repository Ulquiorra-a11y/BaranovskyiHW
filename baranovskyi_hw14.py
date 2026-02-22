# strings = ["apple23", "ban1ana45", "12cherry", "grape3", "blue23berry"]
# res = []
# for item in strings:
#     for char in range(len(item)):
#         if item[char].isdigit():
#             if item[char:].isdigit():
#                 res.append(item)
#             break
# print('Строки с цифрами только в конце: ', res)

# numbers = [1, 3, 6, 9, 10, 12, 15, 19, 20]
# x = int(input("Введите число для удаления кратных ему элементов: "))
# res = []
# for num in numbers:
#     if num % x:
#         res.append(num)
# print('Список без кратных значений:',res)

numbers = [5, 2, 3, 8, 4, 1, 2, 7]
even_numbers = []
res = []
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
even_numbers = sorted(even_numbers,reverse=True)
# print(even_numbers)
for num in numbers:
    if num % 2 == 1:
        res.append(num)
    else:
        res.append(even_numbers.pop(0))
print(res)







