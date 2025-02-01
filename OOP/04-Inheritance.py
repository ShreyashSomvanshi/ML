# add types of inheritance supported by python with example

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

