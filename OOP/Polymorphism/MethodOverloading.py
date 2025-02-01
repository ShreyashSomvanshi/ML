"""
Method overloading allows a class to have multiple methods with the same name but different parameters.
 However, Python does not support method overloading in the traditional sense (like in Java or C++).
 Instead, you can achieve similar behavior using default arguments or variable-length arguments.
"""

class MathOperations:
    def add(self, a, b, c=0):
        return a + b + c

# Usage
math_ops = MathOperations()
print(math_ops.add(2, 3))      # Output: 5
print(math_ops.add(2, 3, 4))   # Output: 9

