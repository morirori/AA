import math
import networkx as nx
import copy as cp
from BreathFirstSearch import BreadthFirstSearch


class FordFulkerson:

    def __init__(self, graph):
        self.initial_graph = graph
        self.reversed_graph = None
        self.residual_graph = graph

    def ford_fulkerson(self, source, target):
        self._init_reversed_graph()
        flow = 0
        path = self.__breath_first_search(source, target)
        while path:
            edge = self._find_edge_with_lowest_capacity(path)
            self.__decrease_flow_in_path(path, self.residual_graph, float(edge["weight"]))
            self.__increase_flow_in_path(path, self.reversed_graph, float(edge["weight"]))
            flow = float(edge["weight"]) + flow
            path = self.__breath_first_search(source, target)
        return flow

    def __breath_first_search(self, source, target):
        bfs = BreadthFirstSearch(self.residual_graph)
        return bfs.find_paths(source, target)

    def _find_edge_with_lowest_capacity(self, path):
        edge_with_lowest_capacity = {"from": 0, "to": 0, "weight": None}
        for i in range(len(path)-1):
            weight = self.residual_graph.get_edge_data(path[i], path[i + 1])["weight"]
            if edge_with_lowest_capacity["weight"] is None or float(weight) <= float(edge_with_lowest_capacity["weight"]):
                edge_with_lowest_capacity = {"from": path[i], "to": path[i+1], "weight": weight}
        return edge_with_lowest_capacity

    def _init_reversed_graph(self):
        self.reversed_graph = nx.DiGraph(self.residual_graph)
        for source, dest, data in self.residual_graph.edges(data=True):
            self.reversed_graph.add_edge(dest, source, weight='0')
            self.reversed_graph.remove_edge(source, dest)

    def __decrease_flow_in_path(self, path, graph: nx.DiGraph, n):
        for i in range(len(path)-1):
            current_weight = float(graph.get_edge_data(path[i], path[i+1])["weight"]) - float(n)
            if current_weight == 0:
                graph.remove_edge(path[i], path[i+1])
            else:
                graph.add_edge(path[i], path[i+1], weight=str(current_weight))

    def __increase_flow_in_path(self, path, graph: nx.DiGraph, n):
        for i in reversed(range(1, len(path))):
            if graph.get_edge_data(path[i], path[i-1]) is not None:
                current_weight = float(graph.get_edge_data(path[i], path[i-1])["weight"]) + float(n)
                graph.add_edge(path[i], path[i-1],  weight=str(current_weight))

