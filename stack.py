class Stack:
    def __init__(self) -> None:
        self.items = []
    
    def is_empty(self):
        if len(self.items) == 0:
            return True
        else:
            return False
        # OR
        # return not self.items

    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peef(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)
    
    def __str__(self):
        return str(self.items)
    
if __name__ == "__main__":
    s = Stack()