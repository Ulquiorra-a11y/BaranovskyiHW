class Person:
    def __init__(self, name):
        self.name = name


    def introduce(self):
        print(f"Hello my name is {self.name}")


# my_person = Person("Alice")
# my_person.introduce()


class Student(Person):
    def __init__(self, name, course):
        super().__init__(name)
        self.course = course

    def introduce(self):
        super().introduce()
        print(f"I'm on course {self.course}")

# student = Student("Alice", 2)
# student.introduce()


class Teacher(Person):
    def __init__(self, name, item):
        super().__init__(name)
        self.item = item

    def introduce(self):
        print(f"Hello, I am professor {self.name}.\nMy subject is {self.item}.")

people = [
    Student("Alice", 2),
    Teacher("Bob", "Mathematic"),
    ]

for person in people:
    person.introduce()