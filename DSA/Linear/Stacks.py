"""
A stack is a linear data structure that follows the Last In First Out (LIFO) principle. You can only add or remove items from the top of the stack.
"""

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return None

    def is_empty(self):
        return len(self.stack) == 0

# Example usage
s = Stack()
s.push(1)
s.push(2)
print(s.pop())  # Output: 2
print(s.peek())  # Output: 1
