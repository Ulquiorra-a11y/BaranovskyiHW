# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def get_area(self):
#         return self.width * self.height
#
# storoni = Rectangle(100, 200)
# print(storoni.get_area())
#
# storoni.width = 40
# storoni.height = 30
#
# print(storoni.get_area())



class Counter:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1
        print(f"Текущее значение: {self.value}")

    def decrement(self):
        self.value -= 1
        print(f"Текущее значение: {self.value}")

    def get_value(self):
        return self.value


counter = Counter()
counter.increment()
counter.increment()
counter.increment()
counter.decrement()
counter.decrement()

print(counter.get_value())