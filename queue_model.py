"""Queue Object (First In, First Out)"""
class Queue:
    def __init__(self, items=None):
        self.items = list(items or [])  # Copy previous values into this object.

    def enqueue(self, value):
        self.items.append(value)  # The last element is the REAR of the queue.

    def dequeue(self):
        return self.items.pop(0) if self.items else None  # Remove the FRONT (index 0).

    def peek(self):
        return self.items[0] if self.items else None  # Look at the FRONT only.

    def is_empty(self):
        return not self.items

    def size(self):
        return len(self.items)

    def clear(self):
        self.items.clear()