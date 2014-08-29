
#!/bin/python
from itertools import izip
from graph_tool.all import *

name = "test2"
g = load_graph(name+".xml")
graph_draw(g, vertex_text=g.vertex_index, vertex_font_size=18,output_size=(200, 200), output=name+".png")

weight = g.edge_properties["weight"]
for v in g.vertices():
   for e in v.out_edges():
       print(str(e) + 'weight: '+str(weight[e]) )
   for w in v.out_neighbours():
       print(w)

   # the edge and neighbours order always match
   for e,w in izip(v.out_edges(), v.out_neighbours()):
       assert(e.target() == w)
