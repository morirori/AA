class BreadthFirstSearch:

    def __init__(self, graph):
        self.graph = graph
        self.paths = list()
        self.queue = list()
        self.already_visited = set()

    def find_paths(self, source, target):
       # temp_paths = list()
        previous = {}
        self.queue.insert(0, source)
     #   temp_paths.append([source])
        finish = True
        while finish:
            examined_vertex = self.queue[0]
            self.already_visited.add(examined_vertex)
            successors = self.graph.successors(examined_vertex)
            for successor in successors:
                self.__add_successor_to_queue(successor)
                self.__set_examined_vertex_as_previous(examined_vertex, successor, previous)
                if successor == target:
                    finish = False
            self.__remove_current_element_from_queue()
            if examined_vertex == target or len(self.queue) == 0:
                finish = False
        self.__find_path(source, target, previous)
        return self.__find_path(source, target, previous)


    def __init_list_of_previous_nodes(self):
        return [{"node": node, "previous": None} for node in self.graph]

    def __add_successor_to_queue(self, successor):
        if successor not in self.already_visited and successor not in self.queue and successor:
            self.queue.append(successor)

    def __remove_current_element_from_queue(self):
        del self.queue[0]

    def __find_path(self, source, target, previous):
        current_vertex = target
        path = []
        if target not in previous.keys():
            return path
        while current_vertex != source:
            previous_vertex = previous[current_vertex]
            path.insert(0, current_vertex)
            current_vertex = previous_vertex
        path.insert(0, current_vertex)
        return path

    def __set_examined_vertex_as_previous(self, examined_vertex, successor, previous):
        if successor not in self.already_visited:
            previous[successor] = examined_vertex
