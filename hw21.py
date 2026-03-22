from collections import Counter


# text = "Programming is fun!"
# def count_letters(text):
#     return dict(Counter(item for item in text.lower() if item.isalpha()))
#
# print(count_letters(text))

students = [("class1", "Alice"), ("class2", "Bob"), ("class1", "Charlie"), ("class3", "Daisy")]

def group_students(students):
    result = {}

    for class_name, student in students:
        result.setdefault(class_name, []).append(student)

    return result
print(group_students(students))
