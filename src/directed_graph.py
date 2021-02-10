class Node:
  def __init__(self, index):
    self.index = index
    self.children = []
    self.parents = []
    self.previous = None
    self.distance = None

class DirectedGraph:
  def __init__(self, edges):
    self.edges = edges
    self.max_index = self.get_max_index()
    self.nodes = [Node(i) for i in range(self.max_index+1)]
    self.build_from_edges()

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
      children = [self.nodes[i] for i in self.get_children(node.index)]
      parents = [self.nodes[i] for i in self.get_parents(node.index)]
      node.children = children
      node.parents = parents
      for child in children:
        if node not in child.parents:
          child.parents.append(node)
      
      for parent in parents:
        if node not in parent.children:
          parent.children.append(node)

  def nodes_breadth_first(self, index):
    queue = [self.nodes[index]]
    visited = []
    while queue != []:
      visiting = queue[0]
      queue = queue[1:]
      visited.append(visiting)
      children = visiting.children
      queue = queue + [child 
                       for child in children 
                       if child not in queue and child not in visited]
    
    return visited

  def nodes_depth_first(self, index):
    stack = [self.nodes[index]]
    visited = []
    while stack != []:
      visiting = stack[0]
      stack = stack[1:]
      visited.append(visiting)
      children = visiting.children
      stack =  [child 
                for child in children 
                if child not in stack and child not in visited] + stack

    return visited

  def set_breadth_first_distance_and_previous(self, starting_node_index): 
    self.nodes[starting_node_index].distance = 0
    queue = [self.nodes[starting_node_index]]
    visited = []
    while queue != []:
      visiting = queue[0]
      current_dist = visiting.distance
      queue = queue[1:]
      visited.append(visiting)
      children = visiting.children
      for child in children:
        if child not in queue and child not in visited:
          child.distance = current_dist + 1
          child.previous = visiting

      queue = queue + [child 
                       for child in children 
                       if child not in queue and child not in visited]

  def calc_distance(self, starting_node_index, ending_node_index):
    self.set_breadth_first_distance_and_previous(starting_node_index)
    return self.nodes[ending_node_index].distance

  def calc_shortest_path(self, starting_node_index, ending_node_index):
    self.set_breadth_first_distance_and_previous(starting_node_index)
    if self.calc_distance(starting_node_index, ending_node_index) != False:
      current_node = self.nodes[ending_node_index]
      path_list = [ending_node_index]
      while current_node.index != starting_node_index:
        current_node = current_node.previous
        path_list.append(current_node.index)
      return path_list[::-1]
    else: 
      return False