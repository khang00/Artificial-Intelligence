from Lab02.queue import Queue

INF = 9999999999


class Graph:
    def __init__(self, number_vertices):
        self.graph_matrix = [[INF] * number_vertices] * number_vertices
        self.distance_matrix = [[INF] * number_vertices] * number_vertices
        self.flag = [0] * number_vertices
        self.number_of_vertices = number_vertices

    def print_distance_matrix(self):
        for row in self.distance_matrix:
            print(row)

    def print_graph_matrix(self):
        for row in self.graph_matrix:
            print(row)

    def add_edge(self, u, v, d):
        self.graph_matrix[u][v] = d
        self.graph_matrix[v][u] = d
        self.graph_matrix[u][u] = 0
        self.graph_matrix[v][v] = 0

    def all_pair_shortest_path(self):
        for vertex in range(0, self.number_of_vertices):
            self.dijkstra(vertex)

    def dijkstra(self, source):
        queue = Queue()
        queue.enqueue(source)
        while not queue.is_empty():
            current_vertex = queue.dequeue()
            if self.flag[current_vertex] == 1:
                for vertex in self.number_of_vertices:
                    if self.distance_matrix[source][current_vertex] + self.distance_matrix[current_vertex][vertex] \
                            < self.distance_matrix[source][vertex]:
                        self.distance_matrix[source][vertex] = self.distance_matrix[source][current_vertex] \
                                                               + self.distance_matrix[current_vertex][vertex]

            else:
                for neighbour in self.get_neighbors(current_vertex):
                    if self.distance_matrix[source][current_vertex] \
                            + self.graph_matrix[current_vertex][neighbour] \
                            < self.distance_matrix[source][neighbour]:
                        print("hello")
                        self.distance_matrix[source][neighbour] \
                            = self.distance_matrix[source][current_vertex] \
                              + self.graph_matrix[current_vertex][neighbour]

        self.flag[source] = 1
        pass

    def get_neighbors(self, u):
        neighbors = []
        for (v, distance) in enumerate(self.graph_matrix[u]):
            if distance != INF:
                neighbors.append(v)
        return neighbors


def main():
    graph = read_graph_from_file("input", "r")
    graph.print_graph_matrix()
    graph.all_pair_shortest_path()
    graph.print_distance_matrix()


def read_graph_from_file(file_name, mode):
    file = open(file_name, mode)
    n = [int(x) for x in next(file).split()]
    graph = Graph(n[0])
    for line in file:
        u, v, d = [int(it) for it in line.strip().split(' ')]
        graph.add_edge(u, v, d)
    file.close()
    return graph


if __name__ == '__main__':
    main()
