# numbers = [4, 7, 3, 7, 8, 3, 4, 2, 7, 3, 8, 4]
# new_numbers = set()
# for num in numbers:
#     if numbers.count(num) > 1:
#         new_numbers.add(num)
#
# print(new_numbers)
# print(sorted(new_numbers, reverse=True))


dict1 = {"a": 1, "b": 2}
dict2 = {"a": 1, "b": 2, "c": 3}

if dict1.items() <= dict2.items():
    print("Первый словарь является подмножеством второго")
else:
    print("Первый словарь не является подмножеством второго")
