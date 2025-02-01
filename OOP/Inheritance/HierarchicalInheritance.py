"""
In hierarchical inheritance, multiple child classes inherit from a single parent class.
 This allows different child classes to share the same parent class.
"""

class Parent:
    def show(self):
        return "This is the parent class"

class Child1(Parent):
    def display(self):
        return "This is the first child class"

class Child2(Parent):
    def greet(self):
        return "This is the second child class"

# Usage
child1 = Child1()
child2 = Child2()
print(child1.show())    # Output: This is the parent class
print(child1.display())  # Output: This is the first child class
print(child2.show())    # Output: This is the parent class
print(child2.greet())    # Output: This is the second child class

