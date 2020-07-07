class Queue:
    def __init__(self):
        self.list = []

    def enqueue(self, value):
        self.list.append(value)

    def dequeue(self):
        if self.is_empty():
            return
        else:
            return self.list.pop(0)

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
