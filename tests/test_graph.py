import sys
sys.path.append('src')
from graph import Graph

edges = [(0,1),(1,2),(1,3),(3,4),(1,4),(4,5)]
graph = Graph(edges)
graph.build_from_edges()

bf = graph.get_nodes_breadth_first(2)
print('Testing method get_nodes_breadth_first...')
assert [node.index for node in bf] == [2, 1, 0, 3, 4, 5]
print('PASSED'), [node.index for node in bf]

df = graph.get_nodes_depth_first(2)
print('Testing method get_nodes_depth_first...')
assert [node.index for node in df] == [2, 1, 0, 3, 4, 5]
print('PASSED')