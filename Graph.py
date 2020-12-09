from Vertex import Vertex
class Graph:
  def __init__(self):
    self.vertices = []
    self.edges = [] 

  def addVertex(self,vertex):
    if vertex not in self.vertices:
      self.vertices.append(vertex)
      for edge in vertex.neighbors:
        self.edges.append((vertex.id, vertex.neighbors[edge].id))
        if vertex.neighbors[edge] not in self.vertices:
          self.addVertex(vertex.neighbors[edge])
  
  def print_path(self,vertex_id):
    vertex = None
    for item in self.vertices:
      if item.id == vertex_id:
        vertex = item
    if vertex == None:
      return('Item does not exist with that id.')
    next_items = list()
    if vertex.neighbors.keys():
      for items in vertex.neighbors.keys():
        next_items.append(items) 
    
    if len(next_items) > 0:
      print(vertex.id + ' goes to ' + str(next_items))
    for neighbor in vertex.neighbors:
      self.print_path(neighbor)

