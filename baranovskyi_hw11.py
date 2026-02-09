user_number = "My number is 123-456-789"
list_user_number = user_number.split()
number = list_user_number[3].split("-")
print(number)
for num in number:
    user_number = user_number.replace(num, "***")
print(user_number)
