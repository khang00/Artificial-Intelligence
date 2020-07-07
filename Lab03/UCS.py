from collections import defaultdict
from Lab03.PriorityQueue import *


class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v, d):
        self.graph[u].append((d, v))

    def ucs(self, s, g):
        if s == g:
            return [s]
        frontier = PriorityQueue()
        expanded = []
        path = defaultdict(list)
        frontier.push(priority=0, item=s)
        while not frontier.is_empty():
            current_node = frontier.pop()
            if self.is_goal(current_node[1], g):
                return self.compute_path(path, g, s)
            expanded.append(current_node)
            self.explore(current_node, frontier, expanded, path)
        return path

    def explore(self, current_node, frontier, expanded, path):
        neighbours = self.graph.get(current_node[1])
        if neighbours is not None:
            for node in neighbours:
                if not self.does_contain(node, expanded):
                    frontier.push(priority=node[0] + current_node[0], item=node[1])
                    path[node[1]] = current_node[1]

    @staticmethod
    def compute_path(path, goal, start):
        computed_path = []
        i = goal
        computed_path.insert(0, goal)
        while path[i] != start:
            computed_path.insert(0, path[i])
            i = path[i]
        computed_path.insert(0, start)
        return computed_path

    @staticmethod
    def does_contain(check_node, arr):
        for node in arr:
            if node[1] == check_node[1]:
                return True
        return False

    @staticmethod
    def is_goal(node, goal):
        return node == goal
                    

g = Graph()
f = open("input.txt", "r")
for line in f:
    u, v, d = [int(it) for it in line.strip().split(' ')]
    g.add_edge(u, v, d)
f.close()

f = open("output.txt", "w")
group = g.ucs(0, 4)
for item in group:
    f.write(str(item) + ' ')
f.close()

print(group)
