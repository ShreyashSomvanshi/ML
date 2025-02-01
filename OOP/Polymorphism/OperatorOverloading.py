"""
Operator overloading allows you to define how operators behave for user-defined classes.
 This means you can use standard operators (like +, -, *, etc.) with your custom objects.
"""

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

# Usage
v1 = Vector(2, 3)
v2 = Vector(4, 5)
v3 = v1 + v2  # Uses the __add__ method
print(v3)     # Output: Vector(6, 8)


"""
Duck Typing: An object is treated as a certain type based on its methods and properties, rather than its actual class.
Method Overriding: A child class provides a specific implementation of a method defined in its parent class.
Method Overloading: Achieved through default or variable-length arguments, allowing methods to accept different numbers of parameters.
Operator Overloading: Custom behavior for standard operators can be defined for user-defined classes.
"""