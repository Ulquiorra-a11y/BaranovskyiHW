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
groups = ["Отличники", "Хорошисты", "Троечники", "Не сдали"]

result = {group: {} for group in groups}

for name, score in students.items():
    if score >= 85:
        result["Отличники"][name] = score
    elif score >= 70:
        result["Хорошисты"][name] = score
    elif score >= 50:
        result["Троечники"][name] = score
    else:
        result["Не сдали"][name] = score

print("Распределение по группам:\n")
print(result)







