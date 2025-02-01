"""
Hybrid inheritance is a combination of two or more types of inheritance.
It can involve multiple inheritance, multilevel inheritance, and hierarchical inheritance.
"""

class Base:
    def show(self):
        return "This is the base class"

class Parent1(Base):
    def display1(self):
        return "This is the first parent class"

class Parent2(Base):
    def display2(self):
        return "This is the second parent class"

class Child(Parent1, Parent2):
    def greet(self):
        return "This is the child class"

# Usage
child = Child()
print(child.show())     # Output: This is the base class
print(child.display1()) # Output: This is the first parent class
print(child.display2()) # Output: This is the second parent class
print(child.greet())    # Output: This is the child class

"""
Single Inheritance: A child class inherits from one parent class.
Multiple Inheritance: A child class inherits from multiple parent classes.
Multilevel Inheritance: A class is derived from another derived class.
Hierarchical Inheritance: Multiple child classes inherit from a single parent class.
Hybrid Inheritance: A combination of two or more types of inheritance.
"""