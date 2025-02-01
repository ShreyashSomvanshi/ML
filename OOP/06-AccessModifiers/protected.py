"""
Protected members are intended to be accessible only within the class and its subclasses. In Python, this is indicated by a single underscore prefix (_).
"""

class BaseClass:
    def __init__(self):
        self._protected_attribute = "I am protected"

    def _protected_method(self):
        return "This is a protected method"

class DerivedClass(BaseClass):
    def access_protected(self):
        return self._protected_attribute

# Usage
obj = DerivedClass()
print(obj.access_protected())  # Output: I am protected
print(obj._protected_method())  # Output: This is a protected method
