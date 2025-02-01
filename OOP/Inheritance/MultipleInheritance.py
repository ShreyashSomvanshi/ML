"""
In multiple inheritance, a child class can inherit from more than one parent class.
 This allows the child class to access attributes and methods from multiple classes.
"""

class Parent1:
    def show1(self):
        return "This is the first parent class"

class Parent2:
    def show2(self):
        return "This is the second parent class"

class Child(Parent1, Parent2):
    def display(self):
        return "This is the child class"

# Usage
child = Child()
print(child.show1())   # Output: This is the first parent class
print(child.show2())   # Output: This is the second parent class
print(child.display())  # Output: This is the child class

