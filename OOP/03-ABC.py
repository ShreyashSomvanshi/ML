# Abstract Base Classes (ABCs) allows to define abstract methods that must be implemented by derived classes.

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

# Creating an object of the derived class
rectangle = Rectangle(5, 10)
print(rectangle.area())  # Output: 50
