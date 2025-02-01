"""
In Python, access modifiers are used to define the visibility and accessibility of class attributes and methods.
While Python does not have strict access modifiers like some other programming languages (e.g., private, protected, public),
 it uses naming conventions to indicate the intended access level.


Public members (attributes and methods) are accessible from outside the class.
By default, all members in a class are public unless specified otherwise.
"""

class MyClass:
    def __init__(self):
        self.public_attribute = "I am public"

    def public_method(self):
        return "This is a public method"

# Usage
obj = MyClass()
print(obj.public_attribute)  # Output: I am public
print(obj.public_method())    # Output: This is a public method
