import heapq


class PriorityQueue:
    def __init__(self):
        self.group = []

    def push(self, item, priority):
        self.update(item, priority)

    def pop(self):
        return heapq.heappop(self.group)

    def update(self, item, priority):
        item_pos = self.find_item(item)
        if item_pos == -1:
            heapq.heappush(self.group, (priority, item))
        elif self.group[item_pos][0] > priority:
            self.group[item_pos] = (priority, item)
            heapq.heapify(self.group)

    def swap(self, pos_a, pos_b):
        tmp = self.group[pos_a]
        self.group[pos_a] = self.group[pos_b]
        self.group[pos_b] = tmp

    def find_item(self, item):
        i = 0
        while i < len(self.group):
            if self.group[i][1] == item:
                return i
            i += 1

        return -1

    def is_empty(self):
        return len(self.group) == 0

    def print(self):
        for item in self.group:
            print(item, end=' ')

    def does_contain(self, item):
        return self.find_item(item) != -1


class PriorityQueueWithFunction(PriorityQueue):

    def __init__(self, priority_function):
        super().__init__()
        self.priority_function = priority_function

    def push(self, weight, item):
        super().update(item=item, priority=self.priority_function(weight))


def main():
    tree = PriorityQueueWithFunction(lambda x: x)
    tree.push(0, 1)
    tree.push(5, 5)
    tree.push(9, 9)
    tree.push(11, 11)
    tree.push(14, 14)
    tree.push(18, 18)
    tree.push(19, 19)
    tree.push(21, 21)
    tree.push(33, 33)
    tree.push(17, 17)
    tree.push(27, 27)
    tree.print()
    print("")
    print(tree.pop())
    tree.print()
    print("")
    print(tree.pop())
    tree.print()
    print("")
    print(tree.pop())
    tree.print()
    print("")
    print(tree.pop())
    tree.print()
    print("")
    print(tree.pop())
    tree.print()
    print("")
    print(tree.pop())
    tree.print()
    print("")
    print(tree.pop())
    tree.print()
    print("")
    print(tree.pop())
    tree.print()
    print("")
    print(tree.pop())
    tree.print()
    print("")
    print(tree.pop())
    tree.print()
    print("")
    print(tree.pop())
    tree.print()
    print("")
    tree.update(0, 55)
    tree.print()


if __name__ == '__main__':
    main()
