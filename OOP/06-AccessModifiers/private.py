"""
Private members are intended to be accessible only within the class itself.
In Python, this is indicated by a double underscore prefix (__).
This name mangling makes it harder to access these members from outside the class.
"""

class MyClass:
    def __init__(self):
        self.__private_attribute = "I am private"

    def __private_method(self):
        return "This is a private method"

    def access_private(self):
        return self.__private_attribute

# Usage
obj = MyClass()
print(obj.access_private())  # Output: I am private

# The following lines will raise an AttributeError
# print(obj.__private_attribute)  # AttributeError
# print(obj.__private_method())    # AttributeError

