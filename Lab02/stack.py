class Stack:
    def __init__(self):
        self.list = []

    def push(self, value):
        self.list.append(value)

    def pop(self):
        if self.is_empty():
            return
        else:
            return self.list.pop()

    def size(self):
        return len(self.list)

    def is_empty(self):
        return self.list == []

    def clear(self):
        return self.list.clear()

    def print(self):
        print(self.list, end=' ')

    def does_contain(self, value):
        if value in self.list:
            return True
        else:
            return False
