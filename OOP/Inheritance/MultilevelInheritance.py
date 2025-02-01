"""
In multilevel inheritance, a class is derived from another derived class, forming a chain of inheritance.
"""

class Grandparent:
    def show(self):
        return "This is the grandparent class"

class Parent(Grandparent):
    def display(self):
        return "This is the parent class"

class Child(Parent):
    def greet(self):
        return "This is the child class"

# Usage
child = Child()
print(child.show())    # Output: This is the grandparent class
print(child.display())  # Output: This is the parent class
print(child.greet())    # Output: This is the child class
