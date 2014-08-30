class Node():

    def __init__(self, node,graph):
        self.vertex = node
	self.ids = graph.vertex_properties["id"]
	self.graph = graph
        
    def getId(self):
        return self.ids[self.vertex]
