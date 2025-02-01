"""
When you define a private member with a double underscore, Python performs name mangling to prevent access from outside the class.
The name of the private member is changed to include the class name.
"""

class MyClass:
    def __init__(self):
        self.__private_attribute = "I am private"

# Usage
obj = MyClass()
# Accessing the private attribute using name mangling
print(obj._MyClass__private_attribute)  # Output: I am private

"""
Public: Accessible from anywhere. No special syntax is needed.
Protected: Intended for internal use within the class and its subclasses. Indicated by a single underscore (_).
Private: Intended for internal use only within the class. Indicated by a double underscore (__), which triggers name mangling.

While Python's access modifiers are more about convention than enforcement, 
they help communicate the intended use of class members and promote better coding practices.
"""