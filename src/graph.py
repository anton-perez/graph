class Node:
  def __init__(self, index):
    self.index = index
    self.neighbors = []
    self.previous = None
    self.distance = None

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
    self.build_from_edges()
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
    self.build_from_edges()
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

  def set_breadth_first_distance_and_previous(self, starting_node_index): 
    self.build_from_edges()
    self.nodes[starting_node_index].distance = 0
    queue = [self.nodes[starting_node_index]]
    visited = []
    while queue != []:
      visiting = queue[0]
      current_dist = visiting.distance
      queue = queue[1:]
      visited.append(visiting)
      neighbors = visiting.neighbors
      for neighbor in neighbors:
        if neighbor not in queue and neighbor not in visited:
          neighbor.distance = current_dist + 1
          neighbor.previous = visiting

      queue = queue + [neighbor 
                       for neighbor in neighbors 
                       if neighbor not in queue and neighbor not in visited]
    
  def calc_distance(self, starting_node_index, ending_node_index):
    self.set_breadth_first_distance_and_previous(starting_node_index)
    return self.nodes[ending_node_index].distance

  def calc_shortest_path(self, starting_node_index, ending_node_index):
    self.set_breadth_first_distance_and_previous(starting_node_index)
    
    current_node = self.nodes[ending_node_index]
    path_list = [ending_node_index]
    while current_node.index != starting_node_index:
      current_node = current_node.previous
      path_list.append(current_node.index)
    return path_list[::-1]

