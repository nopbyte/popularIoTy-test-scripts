popularIoTy-test-scripts
========================

This repository includes test scripts to interact with servioticy reputation module. 

#Install

To install it, you will need to adjust host and port in the script located in the 'setup' folder.  
This scrip will create the index in elastic search (it assumes you have elasticsearch running in localhost, port 9200).

#Running the scripts

## Creating data from graph

The first script you can use is to insert data to resemble a topology represented in a graphml representation (xml file). 
The parameters for this script are given in a configuration file 'general.config', and a command line argument indicating the path of the graphml file containing the service object topology.

A shell script called 'run.sh'can be executed to create the proper documents in elastic search to represent the graph loaded by the python program.

### Format for the graph
The graph represented in the graphml file needs to contain in every edge an id attribute composed of serviceobjectid-streamid. Service objects are named a,b,c, and streams inside service objects are labled with numbers (e.g. 1). (See  two-paths.xml example file). 
In the graph, every node represents a stream inside a service object. And the edges of the graph represent the connections in the topology.

The connections must have two properties: event, and use. Event represents how many times the stream source has generated an event which has triggered an action on the destination service object. On the other hand, use represents the number of times that data generated in the past by the source stream has been used by the destination stream.

### The code

The script to generate data from a graph  will:
*  load the graph from the graphml file
*  store the proper documents in the elasticsearch index, in such a way that if a query is done to ES, the same result of events, and use is obtained.
*  the documents are created with a random timestamp in the range [now, now+timeframe] where timeframe is a parameter specified in the configuration file (in seconds).
*  A representation of the graph is generated in dot format
*  A graphical representation of the graph is created in an image.

Please note that not all the addtional properties in the graphml file, will be stored in the graphical or the dot representation of the graph unfortunatelly :(.

