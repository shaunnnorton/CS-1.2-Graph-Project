class Vertex:
  def __init__(self, id , data=None):
    self.id = id
    self.data = None
    self.neighbors = {} #dictionary of connected verticies
  
  def add_neighbor(self , vertex):
    self.neighbors[vertex.id] = vertex 



  