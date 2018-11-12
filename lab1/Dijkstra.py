import math


class Dijkstra:

    def __init__(self, graph):
        self.graph = graph
        self.__unvisited_set = ()
        self.__distance_table = {}
        self.__previous_vertexes = {}
        self.path = []

    def dijkstra_shortest_path(self, source, target):
        self.__unvisited_set = self.__set_initial_unvisited_set()
        self.__distance_table = self.__set_initial_distance_value(source, )
        current_node = source
        while len(self.__unvisited_set) != 0:
            self.__update_distance_table(current_node)
            self.__unvisited_set.remove(current_node)
            current_node = self.__find_closest_vertex()
            if self.__check_if_finished(target):
                break
        return self.__find_shortest_path(source, target)

    def __update_distance_table(self, current_vertex):
        neighbours = self.graph.successors(current_vertex)
        for neighbour in neighbours:
            new_distance = self.__distance_table[current_vertex] + \
                           self.graph.get_edge_data(current_vertex, neighbour)["weight"]
            if new_distance < self.__distance_table[neighbour]:
                self.__distance_table[neighbour] = new_distance
                self.__previous_vertexes[neighbour] = current_vertex

    def __find_closest_vertex(self):
        return min(self.__distance_table, key=lambda x: self.__distance_table.get(x) if x in self.__unvisited_set else math.inf)

    def __set_initial_unvisited_set(self):
        return set(node for node in self.graph)

    def __find_shortest_path(self, source, target):
        current_vertex = target
        path = []
        total = 0
        while current_vertex != source:
            previous_vertex = self.__previous_vertexes[current_vertex]
            weight = self.graph.get_edge_data(previous_vertex, current_vertex)["weight"]
            total = total + weight
            path.insert(0, current_vertex)
            current_vertex = previous_vertex
        path.insert(0, current_vertex)
        self.path = path
        return {"cost": total, "path": path}

    def __check_if_finished(self, target):
        return True if target not in self.__unvisited_set else False

    def __set_initial_distance_value(self, source):
        distance = {}
        for vertex in self.graph:
            distance[vertex] = math.inf
        distance[source] = 0
        return distance
