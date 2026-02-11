# user_number = "My number is 123-456-789"
# list_user_number = user_number.split()
# number = list_user_number[3].split("-")
# print(number)
# for num in number:
#     user_number = user_number.replace(num, "***")
# print(user_number)
from itertools import count

text = "Programming in python".lower()
use = ''
# counts = 0
for i in range(len(text)):
    char = text[i]
    if char in use: # можно добавить or char == " " что бы не считать пробелы вокруг in
        continue
    use += char
    counts = 0
    for j in range(len(text)):
        if text[j] == char:
            counts += 1
    if counts > 1:
        print(f"'{char}' встречается {counts} раз(а)")
