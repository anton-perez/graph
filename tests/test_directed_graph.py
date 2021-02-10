import sys
sys.path.append('src')
from directed_graph import DirectedGraph

edges = [(0,1),(1,2),(3,1),(4,3),(1,4),(4,5),(3,6)]

directed_graph = DirectedGraph(edges)

print('Testing attribute children...')
assert [[child.index for child in node.children] for node in directed_graph.nodes] == [[1], [2,4], [], [1,6], [3,5], [], []], [[child.index for child in node.children] for node in directed_graph.nodes]
print('PASSED')

print('Testing attribute parents...')
assert [[parent.index for parent in node.parents] for node in directed_graph.nodes] == [[], [0,3], [1], [4], [1], [4], [3]]
print('PASSED')

print('Testing method nodes_breadth_first...')
assert [node.index for node in directed_graph.nodes_breadth_first(4)] == [4, 3, 5, 1, 6, 2]
print('PASSED')

print('Testing method nodes_depth_first...')
assert [node.index for node in directed_graph.nodes_depth_first(4)] == [4, 3, 1, 2, 6, 5]
print('PASSED')
print('Testing method calc_distance...')
assert directed_graph.calc_distance(0,3) == 3
assert directed_graph.calc_distance(3,5) == 3
assert directed_graph.calc_distance(0,5) == 3
assert directed_graph.calc_distance(4,1) == 2
assert directed_graph.calc_distance(2,4) == False
print('PASSED')

print('Testing method calc_shortest_path...')
assert directed_graph.calc_shortest_path(0,3) == [0, 1, 4, 3]
assert directed_graph.calc_shortest_path(3,5) == [3, 1, 4, 5]
assert directed_graph.calc_shortest_path(0,5) == [0, 1, 4, 5]
assert directed_graph.calc_shortest_path(4,1) == [4, 3, 1]
assert directed_graph.calc_shortest_path(2,4) == False
print('PASSED')