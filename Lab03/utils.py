class PriorityQueue:
    def __init__(self, f):
        self.collection = []
        self.collection_function = f

    def push(self, item, priority):
        self.collection.append((priority, item))
        if len(self.collection) > 1:
            self.rebuild_heap_up(len(self.collection) - 1)

    def rebuild_heap_up(self, i):
        if i == 0:
            return
        if self.collection_function(self.collection[(i - 1) // 2], self.collection[i]):
            self.swap(i, (i - 1) // 2)
        self.rebuild_heap_up((i - 1) // 2)

    def pop(self):
        least = self.collection.pop(0)
        if len(self.collection) > 1:
            self.rebuild_heap_down(0)
        return least

    def rebuild_heap_down(self, i):
        if i * 2 + 1 < len(self.collection):
            if self.collection_function(self.collection[i], self.collection[i * 2 + 1]):
                self.swap(i, i * 2 + 1)
            self.rebuild_heap_down(i * 2 + 1)

        elif i * 2 + 2 < len(self.collection):
            if self.collection_function(self.collection[i], self.collection[i * 2 + 1]):
                self.swap(i, i * 2 + 1)
            self.rebuild_heap_down(i * 2 + 1)
        else:
            return

    def swap(self, pos_a, pos_b):
        tmp = self.collection[pos_a]
        self.collection[pos_a] = self.collection[pos_b]
        self.collection[pos_b] = tmp

    def is_empty(self):
        return len(self.collection) == 0

    def update(self, item, priority):
        item_pos = self.find_item(item)
        if item_pos == -1:
            self.push(item, priority)
        elif self.collection_function(self.collection[item_pos], (priority, item)):
            self.collection[item_pos][0] = priority
            self.rebuild_heap_up(item_pos)

    def find_item(self, item):
        i = 0
        while i < len(self.collection):
            if self.collection[i][1] == item:
                return i
            i += 1

        return -1

    def does_contain(self, item):
        return self.find_item(item) != -1

    def print(self):
        for item in self.collection:
            print(item, end=' ')


def main():
    tree = PriorityQueue(lambda a, b: a[0] > b[0])
    tree.push(1, 1)
    tree.push(2, 2)
    tree.push(3, 3)
    tree.push(4, 4)
    tree.push(0, 0)
    tree.print()


if __name__ == '__main__':
    main()
