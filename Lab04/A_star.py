from collections import defaultdict
from Lab03.PriorityQueue import PriorityQueue


class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v, l):
        self.graph[u].append((l, v))

    def A_star(self, s, g, heuristics):
        if s == g:
            return [s]
        frontier = PriorityQueue()
        expanded = []
        cost = 0
        path = defaultdict(list)
        frontier.push(priority=heuristics[s] + 0, item=s)
        while not frontier.is_empty():
            current_node = frontier.pop()
            cost = cost + current_node[0] - heuristics[current_node[1]] - cost
            if self.is_goal(current_node[1], heuristics):
                return cost
            expanded.append(current_node)
            self.explore(current_node, frontier, expanded, path, heuristics)
        return path

    def explore(self, current_node, frontier, expanded, path, heuristics):
        neighbours = self.graph.get(current_node[1])
        if neighbours is not None:
            for node in neighbours:
                if not self.does_contain(node, expanded):
                    frontier.push(priority=heuristics[node[1]] + node[0] + current_node[0] - heuristics[current_node[1]], item=node[1])
                    path[node[1]] = current_node

    @staticmethod
    def compute_path(path, goal, start):
        computed_path = []
        cost = 0
        i = goal
        computed_path.insert(0, goal)
        while path[i][1] != start:
            computed_path.insert(0, path[i][1])
            cost = cost + path[i][0]
            i = path[i][1]
        computed_path.insert(0, start)
        return computed_path, cost

    @staticmethod
    def does_contain(check_node, arr):
        for node in arr:
            if node[1] == check_node[1]:
                return True
        return False

    def is_goal(self, node, heuristics):
        return heuristics[node] == 0


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
f.write(str(g.A_star(start, goal, heuristics)))
f.close()

print(g.A_star(start, goal, heuristics))
