from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()
    
    def __str__(self):
        return str(self.items)

    def is_empty(self):
        return not self.items
    
    def enqueue(self, item):
        return self.items.append(item)
    
    def dequeue(self):
        return self.items.popleft()
    
    def size(self):
        return len(self.items)
    
    def peek(self):
        return self.items[0] 
    
