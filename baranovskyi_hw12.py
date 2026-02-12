# numbers = [1245.4435, -302.1403, 87459.99, -520.8265, 1450.001]
# summa = 0
# for x in numbers:
#     if x > 0:
#         summa += x
# print(f'Сумма положительных чисел: ${summa:,.2f} ')
# print('Сумма положительных чисел: ${:,.2f}'.format(summa))

data_list = ["John 23 12345.678", "Alice 30 200.50", "Bob 35 15000.3","Charlie 40 500.75"]
for x in data_list:
    y,a,b = x.split()
    print(f"Имя: {y:10} | Возраст: {a:>3} | Баланс: {float(b):10.2f}")


