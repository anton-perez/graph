class Node:
  def __init__(self, index):
    self.index = index
    self.neighbors = []

class Graph:
  def __init__(self, edges):
    self.edges = edges
    self.max_index = self.get_max_index()
    self.nodes = [Node(i) for i in range(self.max_index+1)]

  def get_neighbors(self, index):
    neighbors = []
    for edge in self.edges:
      if edge[0] == index:
        neighbors.append(edge[1])
      elif edge[1] == index:
        neighbors.append(edge[0])
    return neighbors

  def get_max_index(self):
    max = self.edges[0][0]
    for edge in self.edges:
      if edge[0] > max:
        max = edge[0]
      elif edge[1] > max:
        max = edge[1]
    return max

  def build_from_edges(self):
    for node in self.nodes:
      neighbors = [self.nodes[i] for i in self.get_neighbors(node.index)]
      node.neighbors = neighbors
      for neighbor in neighbors:
        if node not in neighbor.neighbors:
          neighbor.neighbors.append(node)
      

  def get_nodes_breadth_first(self, initial_node):
    queue = [self.nodes[initial_node]]
    visited = []
    while queue != []:
      visiting = queue[0]
      queue = queue[1:]
      visited.append(visiting)
      neighbors = visiting.neighbors
      queue = queue + [neighbor 
                       for neighbor in neighbors 
                       if neighbor not in queue and neighbor not in visited]
    return visited

  def get_nodes_depth_first(self, initial_node):
    stack = [self.nodes[initial_node]]
    visited = []
    while stack != []:
      visiting = stack[0]
      stack = stack[1:]  
      visited.append(visiting)
      neighbors = visiting.neighbors
      stack = [neighbor 
               for neighbor in neighbors 
               if neighbor not in stack and neighbor not in visited] + stack
    return visited