import networkx as nx
from DataHelper import DataHelper
from FordFulkerson import FordFulkerson


data = DataHelper.read_data("data//graph.txt")
graph = nx.DiGraph()
graph.add_weighted_edges_from(data)
x = FordFulkerson(graph)
result = x.ford_fulkerson('10', '60')
print("flow: {}".format(result))


source = "10"
nodes_num = max(graph.nodes)
max_result = 0
nodes = list()
for i in range(int(nodes_num)):
    graph = nx.DiGraph()
    graph.add_weighted_edges_from(data)
    x = FordFulkerson(graph)
    result = x.ford_fulkerson(source, str(i))
    if result >= max_result:
        max_result = result
        nodes.append(i)
print("nodes: {} flow: {}".format(nodes, max_result))


