import sys
sys.path.append('src')
from tree import Tree

# edges = [('a','c'), ('e','g'), ('e','i'), ('e','a'), ('g','b'), ('a','d'), ('d','f'), ('f','h'), ('d','j'), ('c','k')]
# tree = Tree(edges)
# tree.build_from_edges()

# print('Testing attribute root...')
# assert tree.root.value == 'e'
# print('PASSED')

# print('Testing method build_from_edges...')
# print('Testing children of e...')
# assert [node.value for node in tree.root.children] == ['g', 'i', 'a']

# print('Testing children of g...')
# assert [node.value for node in tree.root.children[0].children] == ['b']

# print('Testing children of i...')
# assert [node.value for node in tree.root.children[1].children] == []

# print('Testing children of a...')
# assert [node.value for node in tree.root.children[2].children] == ['c', 'd']

# print('Testing children of c...')
# assert [node.value for node in tree.root.children[2].children[0].children] == ['k'], [node.value for node in tree.root.children[0].children[0].children]

# print('Testing children of d...')
# assert [node.value for node in tree.root.children[2].children[1].children] == ['f', 'j']

# print('Testing children of b...')
# assert [node.value for node in tree.root.children[0].children[0].children] == []

# print('Testing children of k...')
# assert [node.value for node in tree.root.children[2].children[0].children[0].children] == []

# print('Testing children of j...')
# assert [node.value for node in tree.root.children[2].children[1].children[1].children] == []

# print('Testing children of f...')
# assert [node.value for node in tree.root.children[2].children[1].children[0].children] == ['h']

# print('Testing children of h...')
# assert [node.value for node in tree.root.children[2].children[1].children[0].children[0].children] == []
# print('PASSED')


# edges = [('a','c'), ('e','g'), ('e','i'), ('e','a'), ('d','b'), ('a','d'), ('d','f'), ('f','h'), ('d','j'), ('d','k')]
# tree = Tree(edges)
# tree.build_from_edges()
# nodes = tree.nodes_breadth_first()
# print('Testing method nodes_breadth_first...')
# assert [node.value for node in nodes] == ['e', 'g', 'i', 'a', 'c', 'd', 'b', 'f', 'j', 'k', 'h']
# print('PASSED')

# nodes = tree.nodes_depth_first()
# print('Testing method nodes_depth_first...')
# assert [node.value for node in nodes] == ['e', 'g', 'i', 'a', 'c', 'd', 'b', 'f', 'h', 'j', 'k']
# print('PASSED')

node_values = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
edges = [(0,2), (4,6), (4,8), (4,0), (3,1), (0,3), (3,5), (5,7), (3,9), (3,10)]

tree = Tree(edges, node_values)
tree.build_from_edges()

print('Testing indices with Test Case 1:')
assert tree.root.value == 'e'
assert tree.root.index == 4

children = set(tree.root.children)

grandchildren = set([])
for child in children:
  grandchildren = grandchildren.union(set(child.children))

great_grandchildren = set([])
for grandchild in grandchildren:
  great_grandchildren = great_grandchildren.union(set(grandchild.children))

great_great_grandchildren = set([])
for great_grandchild in great_grandchildren:
  great_great_grandchildren = great_great_grandchildren.union(set(great_grandchild.children))

assert {node.index for node in children} == {0, 8, 6}
assert {node.value for node in children} == {'a', 'i', 'g'}

assert {node.index for node in grandchildren} == {2, 3}
assert {node.value for node in grandchildren} == {'c', 'd'}

assert {node.index for node in great_grandchildren} == {1, 9, 5, 10}
assert {node.value for node in great_grandchildren} == {'b', 'j', 'f', 'k'}

assert {node.index for node in great_great_grandchildren} == {7}
assert {node.value for node in great_great_grandchildren} == {'h'}
print('PASSED')


node_values = ['a', 'b', 'a', 'a', 'a', 'b', 'a', 'b', 'a', 'b', 'b']

edges = [(0,2), (4,6), (4,8), (4,0), (3,1), (0,3), (3,5), (5,7), (3,9), (3,10)]

tree = Tree(edges, node_values)
tree.build_from_edges()

print('Testing indices with Test Case 2:')
assert tree.root.value == 'a'
assert tree.root.index == 4

children = set(tree.root.children)

grandchildren = set([])
for child in children:
  grandchildren = grandchildren.union(set(child.children))

great_grandchildren = set([])
for grandchild in grandchildren:
  great_grandchildren = great_grandchildren.union(set(grandchild.children))

great_great_grandchildren = set([])
for great_grandchild in great_grandchildren:
  great_great_grandchildren = great_great_grandchildren.union(set(great_grandchild.children))

assert {node.index for node in children} == {0, 8, 6}
assert {node.value for node in children} == {'a', 'a', 'a'}

assert {node.index for node in grandchildren} == {2, 3}
assert {node.value for node in grandchildren} == {'a', 'a'}

assert {node.index for node in great_grandchildren} == {1, 9, 5, 10}
assert {node.value for node in great_grandchildren} == {'b', 'b', 'b', 'b'}

assert {node.index for node in great_great_grandchildren} == {7}
assert {node.value for node in great_great_grandchildren} == {'b'}
print('PASSED')