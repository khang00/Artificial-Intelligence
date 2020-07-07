class Tree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def print(self):
        print(self.value)
        if self.left is not None:
            self.left.print()
        if self.right is not None:
            self.right.print()

    def insert(self, value):
        if value < self.value:
            if self.left is not None:
                self.left.insert(value)
            else:
                self.left = Tree(value)
        else:
            if self.right is not None:
                self.right.insert(value)
            else:
                self.right = Tree(value)
