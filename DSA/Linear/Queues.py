"""
A queue is a linear data structure that follows the First In First Out (FIFO) principle. You can add items to the back and remove items from the front.
"""

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return None

    def front(self):
        if not self.is_empty():
            return self.queue[0]
        return None

    def is_empty(self):
        return len(self.queue) == 0

# Example usage
q = Queue()
q.enqueue(1)
q.enqueue(2)
print(q.dequeue())  # Output: 1
print(q.front())  # Output: 2

"""
Arrays are simple and efficient for indexed access but have a fixed size.
Linked Lists provide dynamic sizing and efficient insertions/deletions but have higher memory overhead.
Stacks are useful for backtracking algorithms and function calls.
Queues are used in scenarios like scheduling and buffering.
"""