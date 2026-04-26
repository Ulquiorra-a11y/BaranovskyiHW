import json
from datetime import datetime


def calculate_age(birth_date: str, enrollment_date: str) -> int:
    '''
    Calculate age at enrollment
    :param birth_date: date of birth
    :param enrollment_date: date of enrollment
    :return:age at enrollment
    '''
    b = datetime.strptime(birth_date, "%d.%m.%Y")
    e = datetime.strptime(enrollment_date, "%d.%m.%Y")

    age = e.year - b.year
    if (e.month, e.day) < (b.month, b.day):
        age -= 1

    return age


try:
    with open("student_courses.json", "r", encoding="utf-8") as file:
        students = json.load(file)
except FileNotFoundError:
    print("File not found")
    exit()


total_students = len(students)
total_age = 0
courses_count = {}

for student in students:
    age = calculate_age(student["birth_date"], student["enrollment_date"])
    total_age += age

    for course in student["courses"]:
        courses_count[course] = courses_count.get(course, 0) + 1


average_age = round(total_age / total_students, 2) if total_students else 0


report = {
    "total_students": total_students,
    "average_age_at_enrollment": round(average_age),
    "courses": courses_count
}


with open("student_courses_report.json", "w", encoding="utf-8") as file:
    json.dump(report, file, ensure_ascii=False, indent=4)


print("Отчёт сохранён в student_courses_report.json")