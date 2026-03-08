# numbers = [4, 7, 3, 7, 8, 3, 4, 2, 7, 3, 8, 4]
# new_numbers = set()
# for num in numbers:
#     if numbers.count(num) > 1:
#         new_numbers.add(num)
# result = list(new_numbers)
# print(result)
# result.sort(reverse=True)
# print(result)

dict1 = {"a": 1, "b": 2}
dict2 = {"a": 1, "b": 2, "c": 3}

res = True
for key in dict1:
    if dict1[key] != dict2[key]:
        res = False
        break
if res:
    print("Первый словарь является подмножеством второго")
