# x = input('Символ: ')
# y = ord(x)
# is_ascii = 128 > y
# print("Код Unicode: ", y)
# print('ASCII символ: ', is_ascii)

# st = input("Введите строку: ")
# symbol = input("Введите символ: ")
# count = st.count(symbol)
# print("Символ встречается", count, "раз(а)")

# st = input("Введите строку: ")
# start = int(input("Введите начальный индекс: "))
# end = int(input("Введите конечный индекс: "))
# length = end - start
# st2 = st[start:end]
# if len(st2) < length:
#     st2 += "_" * (length - len(st2))
# print('Подстрока: ' , st2)

stroka = input("Введите строку: ")

res = ''
i = len(stroka) - 1

while i >= 0:
    if not stroka[i].isdigit():
        res += stroka[i]
    i -= 1

print("Результат:", res)


