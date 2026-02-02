# a = int(input('Введите первое число: '))
# b = int(input("Введите второе число: "))
# c = int(input("Введите третье число: "))
# if a <= b and a <= c:
#     if b <= c:
#         print(a, b, c, sep=',')
#     else:
#         print(a, c, b, sep=',')
# elif b <= a and b <= c:
#     if a <= c:
#         print(b, a, c, sep=',')
#     else:
#         print(b, c, a, sep=',')
# elif c <= b and c <= a:
#     if b <= a:
#         print(c, b, a, sep=',')
#     else:
#         print(c, a, b, sep=',')


year = int(input('Введите год: '))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('Год является високосным')
else:
    print('Год не является високосным')