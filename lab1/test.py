import networkx as nx
from DataHelper import DataHelper
from Dijkstra import Dijkstra

data = DataHelper.read_data("data//graph.txt")
graph = nx.DiGraph()
graph.add_weighted_edges_from(data)
dijkstra = Dijkstra(graph)
print(dijkstra.dijkstra_shortest_path(1, 20))
