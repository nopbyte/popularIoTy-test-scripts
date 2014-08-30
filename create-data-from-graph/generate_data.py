#!/usr/bin/python
import os, sys
from itertools import izip
from graph_tool.all import *
import ConfigParser
import io

#my own code
lib_path = os.path.abspath('./graph')
sys.path.append(lib_path)
from node import *
from elasticsearch import *

#Verifications
def check_arguments():
 if len(sys.argv) == 1:
   print('usage: '+ sys.argv[0]+ 'path__file')
   print('The file referenced in the argument must be placed inside the a folder called graphml!')
   exit()

#MISC
def log(s):
 print s

def loadConfig():
 config = ConfigParser.RawConfigParser(allow_no_value=True)
 f = open('general.config', 'r+')
 config.readfp(io.BytesIO(f.read()))
 f.close()
 return config

#Error 
def wrong_id(node):
 print "Error: Id of the node "+node.getId()+" doesnt have the format 'soid'-'streamid'! "
 exit()


def main():
 check_arguments()
 name = sys.argv[1]
 config = loadConfig()
 g = load_graph("graphml/"+name)
 #graph_draw(g, vertex_text=g.vertex_index, vertex_font_size=18,output_size=(200, 200), output=name+".png")
 es = ES(config)

 #ids = g.vertex_properties["id"]
 events = g.edge_properties["event"]
 use = g.edge_properties["use"]
 for e in g.edges():
    src = Node(e.source(), g)
    dest = Node(e.target(),g)
    parsed_src = src.getId().partition('-')
    if parsed_src[2] == '':
       wrong_id(node)
    parsed_dest = dest.getId().partition('-')
    if parsed_dest[2] == '':
       wrong_id(dest)
    print('insert data for source soid:stream %s:%s => soid:stream: %s:%s. Events=%f. Use=%f'
                      %(parsed_src[0], parsed_src[2], parsed_dest[0], parsed_dest[2], events[e], use[e]))


 #draw
 graph_draw(g, vertex_text=g.vertex_properties['id'],  
     vertex_font_size=16,output_size=(200, 200), 
     output=name+".png")
 #export as dot
 g.save(name+'.dot')


if __name__ == "__main__":
    main()
