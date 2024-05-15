class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        # tam = len(self.items)
        # if tam == 0:
        #     return True
        # else:
        #     return False
        return not self.items

    def __str__(self):
        return str(self.items)

    def push(self, item):
        return self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)
  




