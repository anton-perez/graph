class Node:
  def __init__(self, value):
    self.value = value
    self.children = []

class Tree:
  def __init__(self, edges):
    self.edges = edges
    self.root = self.get_root()

  def get_children(self, node):
    children = []
    for edge in self.edges:
      if edge[0] == node:
        children.append(edge[1])
    return children

  def get_parents(self, node):
    parents = []
    for edge in self.edges:
      if edge[1] == node:
        parents.append(edge[0])
    return parents

  def get_root(self):
    for edge in self.edges:
      grandparent = self.get_parents(edge[0])
      if grandparent == []:
        return Node(edge[0])

  def build_from_edges(self):
    current_nodes = [self.root]
    while current_nodes != []:
      current_children = []
      for node in current_nodes:
        children = [Node(child) for child in self.get_children(node.value)] 
        node.children = children
        current_children += children
      current_nodes = current_children


edges = [('a','c'), ('e','g'), ('e','i'), ('e','a'), ('g','b'), ('a','d'), ('d','f'), ('f','h'), ('d','j'), ('c','k')]
tree = Tree(edges)
tree.build_from_edges()

print('Testing attribute root...')
assert tree.root.value == 'e'
print('PASSED')

print('Testing method build_from_edges...')
print('Testing children of e...')
assert [node.value for node in tree.root.children] == ['g', 'i', 'a']

print('Testing children of g...')
assert [node.value for node in tree.root.children[0].children] == ['b']

print('Testing children of i...')
assert [node.value for node in tree.root.children[1].children] == []

print('Testing children of a...')
assert [node.value for node in tree.root.children[2].children] == ['c', 'd']

print('Testing children of c...')
assert [node.value for node in tree.root.children[2].children[0].children] == ['k'], [node.value for node in tree.root.children[0].children[0].children]

print('Testing children of d...')
assert [node.value for node in tree.root.children[2].children[1].children] == ['f', 'j']

print('Testing children of b...')
assert [node.value for node in tree.root.children[0].children[0].children] == []

print('Testing children of k...')
assert [node.value for node in tree.root.children[2].children[0].children[0].children] == []

print('Testing children of j...')
assert [node.value for node in tree.root.children[2].children[1].children[1].children] == []

print('Testing children of f...')
assert [node.value for node in tree.root.children[2].children[1].children[0].children] == ['h']

print('Testing children of h...')
assert [node.value for node in tree.root.children[2].children[1].children[0].children[0].children] == []
print('PASSED')