class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit

    def isEmpty(self):
        if(self.items):
            return False
        else:
            return True

    def push(self, item):
        if not self.full():
            self.items.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            return None

    def peek(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)

    def full(self):
        if len(self.items) >= self.limit:
            return True
        else:
            return False

    def search(self, target):
        length = 0
        i = len(self.items) - 1

        while i >= 0:
            if self.items[i] == target:
                return length
            else:
                length += 1
                i -= 1
        
        return -1

