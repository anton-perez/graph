class Node:
  def __init__(self, index):
    self.value = None
    self.index = index
    self.children = []

class Tree:
  def __init__(self, edges, node_values):
    self.edges = edges
    self.node_values = node_values
    self.root = self.get_root()

  def get_children(self, index):
    children = []
    for edge in self.edges:
      if edge[0] == index:
        children.append(edge[1])
    return children

  def get_parents(self, index):
    parents = []
    for edge in self.edges:
      if edge[1] == index:
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
        node.value = self.node_values[node.index]
        children = [Node(child) for child in self.get_children(node.index)] 
        node.children = children
        current_children += children
      current_nodes = current_children
  
  def nodes_breadth_first(self):
    queue = [self.root]
    visited = []
    while queue != []:
      visiting = queue[0]
      queue = queue[1:]
      visited.append(visiting)
      children = visiting.children
      queue = queue + children
    
    return visited

  def nodes_depth_first(self):
    stack = [self.root]
    visited = []
    while stack != []:
      visiting = stack[0]
      stack = stack[1:]
      visited.append(visiting)
      children = visiting.children
      stack = children + stack
     
    return visited

