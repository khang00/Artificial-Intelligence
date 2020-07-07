from collections import defaultdict
from stack import Stack


class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def depth_first_search(self, start):
        frontier = Stack()
        expanded = []
        frontier.push(start)
        while not frontier.is_empty():
            current_node = frontier.pop()
            expanded.append(current_node)
            self.explore(current_node, frontier, expanded)
        return expanded

    def explore(self, node, frontier, expanded):
        neighbours = self.graph.get(node)
        if neighbours is not None:
            for node in neighbours[::-1] or []:
                if node not in expanded and not frontier.does_contain(node):
                    frontier.push(node)


g = Graph()

f = open("input.txt", "r")
for line in f:
    u, v = [int(it) for it in line.strip().split(' ')]
    g.add_edge(u, v)
f.close()

f = open("output.txt", "w")
group = g.depth_first_search(0)
for item in group:
    f.write(str(item) + ' ')
f.close()
