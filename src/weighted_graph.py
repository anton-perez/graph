import sys
sys.path.append('src')
from graph import Graph

class Node:
  def __init__(self, index):
    self.index = index
    self.value = None
    self.neighbors = []
    self.previous = None
    self.d = 99999999

class WeightedGraph:
  def __init__(self, weights, values):
    self.weights = weights
    self.values = values 
    self.edges = [edge for edge in self.weights]
    self.max_index = self.get_max_index()
    self.nodes = [Node(i) for i in range(self.max_index+1)]
    self.build_from_edges()

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

  def set_breadth_first_distance_and_previous(self, starting_node_index): 
    self.build_from_edges()
    self.nodes[starting_node_index].d = 0
    queue = [self.nodes[starting_node_index]]
    visited = []
    while queue != []:
      visiting = queue[0]
      current_dist = visiting.d
      for node in queue:
        if node.d < current_dist:
          visiting = node
          current_dist = node.d
      queue = [node for node in queue if node != visiting]
      visited.append(visiting)
      neighbors = visiting.neighbors
      for neighbor in neighbors:
        edge = (visiting.index, neighbor.index) if (visiting.index, neighbor.index) in self.edges else (neighbor.index, visiting.index)
        weight = self.weights[edge]
        if neighbor not in visited and current_dist + weight < neighbor.d:
          neighbor.d = current_dist + weight

      queue = queue + [neighbor 
                       for neighbor in neighbors 
                       if neighbor not in visited]
    
  def calc_distance(self, starting_node_index, ending_node_index):
    self.set_breadth_first_distance_and_previous(starting_node_index)
    return self.nodes[ending_node_index].d

  def calc_shortest_path(self, starting_node_index, ending_node_index):
    self.set_breadth_first_distance_and_previous(starting_node_index)
    shortest_path_edges = []
    for edge in self.edges:
      weight = self.weights[edge]
      node_a = self.nodes[edge[0]]
      node_b = self.nodes[edge[1]]

      if abs(node_a.d - node_b.d) == weight:
        shortest_path_edges.append(edge)

    return Graph(shortest_path_edges).calc_shortest_path(starting_node_index, ending_node_index)