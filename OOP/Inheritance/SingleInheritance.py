"""
In single inheritance, a child class inherits from one parent class.
This is the simplest form of inheritance
"""

class Parent:
    def show(self):
        return "This is the parent class"

class Child(Parent):
    def display(self):
        return "This is the child class"

# Usage
child = Child()
print(child.show())    # Output: This is the parent class
print(child.display()) # Output: This is the child class

