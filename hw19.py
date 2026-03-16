# data = {"a": 1, "b": 2, "c": 1, "d": 3}
# reversed_data = {}
#
# for key, value in data.items():
#     if value not in reversed_data:
#         reversed_data[value] = []
#     reversed_data[value].append(key)
#
# print("Перевернутый словарь:", reversed_data)

# words = ["anna", "bennet", "john"]
# result = {word: {letter: word.count(letter) for letter in set(word)} for word in words}
# print(result)

students = {"Аня": 92, "Боря": 76, "Ваня": 65, "Галя": 48, "Дима": 88, "Ева": 54}

result = {
    "Отличники": {k: v for k, v in students.items() if v >= 85},
    "Хорошисты": {k: v for k, v in students.items() if 70 <= v <= 84},
    "Троечники": {k: v for k, v in students.items() if 50 <= v <= 69},
    "Не сдали": {k: v for k, v in students.items() if v < 50}
}
print(result)







