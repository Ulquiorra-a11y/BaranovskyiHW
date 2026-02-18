# numbers = (3, 7, 2, 8, 5, 10, 1)
# res = []
# max_num = ""
# for number in numbers:
#     if max_num == "" or number > max_num:
#         res.append(number)
#         max_num = number
# print("Кортеж по возрастанию:", tuple(res))

numbers = (1, 2, 3, 4, 2, 5, 3, 6, 4, 2, 9)
tmp = []
for number in range(len(numbers)):
    if numbers[number] not in tmp:
        tmp.append(numbers[number])
        indx = []
        for i in range(len(numbers)):
            if numbers[i] == numbers[number]:
                indx.append(i)
        if len(indx) > 1:
            print(f"Индексы элемента {numbers[number]}:", *indx)
