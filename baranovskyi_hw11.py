# user_number = "My number is 123-456-789"
# list_user_number = user_number.split()
# number = list_user_number[3].split("-")
# for num in number:
#     user_number = user_number.replace(num, "***")
# print(user_number)

# text = "Programming in python".lower()
# use = ''
#
# for i in range(len(text)):
#     char = text[i]
#     if char in use: # можно добавить or char == " " что бы не считать пробелы вокруг in
#         continue
#     use += char
#     counts = 0
#     for j in range(len(text)):
#         if text[j] == char:
#             counts += 1
#     if counts > 1:
#         print(f"'{char}' встречается {counts} раз(а)")


text = "I have 5 apples and 10 oranges, price is 0.5 each. Card number is ....3672.".split()

for i in text:
    x = i.rstrip('.')
    if x.replace('.', '', 1).isdigit():
        i = float(x) * 10
    print(i, end=" ")






