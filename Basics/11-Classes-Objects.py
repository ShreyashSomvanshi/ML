# Class with __init__ and __str__ methods
# The __init__ method initializes an object's attributes, and
# the __str__ method defines how an object is represented as a string.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old."

# Creating an object
person = Person("Alice", 30)
print(person)  # Output: Alice is 30 years old.


# Class definition
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        return f"{self.name} says woof!"

# Creating an object
my_dog = Dog("Buddy")
print(my_dog.bark())

# Using isinstance()
x = 10
print(isinstance(x, int))  # Output: True
print(isinstance(x, (float, str)))  # Output: False


