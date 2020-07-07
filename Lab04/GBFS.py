from collections import defaultdict
from Lab03.PriorityQueue import PriorityQueue


class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v, l):
        self.graph[u].append((l, v))

    def gbfs(self, s, g,heuristics):
        if s == g:
            return [s]
        frontier = PriorityQueue()
        expanded = []
        path = defaultdict(list)
        frontier.push(priority=heuristics[s], item=s)
        while not frontier.is_empty():
            current_node = frontier.pop()
            if self.is_goal(current_node[1], heuristics):
                return self.compute_path(path, g, s)
            expanded.append(current_node)
            self.explore(current_node, frontier, expanded, path, heuristics)
        return path

    def explore(self, current_node, frontier, expanded, path, heuristics):
        neighbours = self.graph.get(current_node[1])
        if neighbours is not None:
            for node in neighbours:
                if not self.does_contain(node, expanded):
                    frontier.push(priority=heuristics[node[1]], item=node[1])
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

    def is_goal(self, node, heuristics):
        return heuristics[node] == 0

    def calculate_heuristic(self, path, heuristics):
        cost = 0
        for node in path:
            cost = cost + heuristics[node]
        return cost


g = Graph()
heuristics = []
with open('input', 'r') as f:
    n, m = [int(x) for x in next(f).split()]
    for i in range(m):
        u, v, l = [int(x) for x in next(f).split()]
        g.add_edge(u, v, l)
    for i in range(n):
        h = [int(x) for x in next(f).split()]
        heuristics.append(h.pop())
    start, goal = [int(x) for x in next(f).split()]

f = open("output.txt", "w")
f.write(str(g.calculate_heuristic(g.gbfs(start, goal, heuristics), heuristics)))
f.close()

print(g.calculate_heuristic(g.gbfs(start, goal, heuristics), heuristics))
