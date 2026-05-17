from math import pi
from abc import ABC, abstractmethod


class InvalidSizeError(ValueError):
    pass

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length: float, width: float):
        if length <= 0 or width <= 0:
            raise InvalidSizeError('Число должно быть больше 0!')
        self.length = length
        self.width = width

    def area(self) -> float:
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius: float):
        if radius <= 0:
            raise InvalidSizeError('Число должно быть больше 0!')
        self.radius = radius

    def area(self) -> float:
        return pow(self.radius, 2) * pi

shapes = [Circle(3), Rectangle(4, 5)]
for shape in shapes:
    print(f"Area: {shape.area():.2f}")

try:
    shapes = [Circle(0), Rectangle(4, 5)]
    for shape in shapes:
        print(f"Area: {shape.area():.2f}")
except InvalidSizeError as e:
    print(f"InvalidSizeError: {e}")