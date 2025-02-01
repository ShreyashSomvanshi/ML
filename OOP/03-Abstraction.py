"""
Abstraction is the concept of hiding the complex implementation details and showing only the essential features of the object.
 It can be achieved using abstract classes and interfaces.
"""
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

# Usage
shapes = [Rectangle(10, 5), Circle(7)]
for shape in shapes:
    print(f"Area: {shape.area()}")
