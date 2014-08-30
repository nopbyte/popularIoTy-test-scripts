#!/usr/bin/python
import os, sys
from itertools import izip
from graph_tool.all import *

#my own code
lib_path = os.path.abspath('./graph')
sys.path.append(lib_path)
from node import *

#Read arguments
if len(sys.argv) == 1:
   print('usage: '+ sys.argv[0]+ 'path__file')
   print('The file referenced in the argument must be placed inside the a folder called graphml!')
   exit()

name = sys.argv[1]
g = load_graph("graphml/"+name)
#graph_draw(g, vertex_text=g.vertex_index, vertex_font_size=18,output_size=(200, 200), output=name+".png")

#ids = g.vertex_properties["id"]
events = g.edge_properties["event"]
use = g.edge_properties["use"]
for v in g.vertices():
   node = Node(v,g)
   print(node.getId())
   print(type(v))
#   print (ids[v])
   for e in v.out_edges():
       print(str(e) + 'event: '+str(events[e]) )
       print(str(e) + 'use: '+str(use[e]) )
   for w in v.out_neighbours():
       print(w)

   # the edge and neighbours order always match
   for e,w in izip(v.out_edges(), v.out_neighbours()):
       assert(e.target() == w)


#draw
graph_draw(g, vertex_text=g.vertex_properties['id'], vertex_font_size=18,output_size=(200, 200), output=name+".png")
#export as dot
g.save(name+'.dot')
