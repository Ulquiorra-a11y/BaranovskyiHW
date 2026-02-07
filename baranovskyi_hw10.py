# weights = [50, 10, 5, 2, 1]
# need = int(input("Введите стоимость: "))
#
# for coin in weights:
#     n = need // coin
#     if n:
#         print('Внесите монеты номиналом', coin, ':', n)
#         need %= coin
#

numbers = [4, 9, 1, 7, 2, 5, 0, 3, 7, 1, 3]
print('Изначальный список:', numbers)

for i in range(len(numbers)):
    if numbers[i] % 2:
        numbers[i] = numbers[i] ** 2
print('Измененный список:', numbers)