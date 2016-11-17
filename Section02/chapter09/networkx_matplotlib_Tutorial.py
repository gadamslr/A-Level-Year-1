# Creating a Graph

import networkx as nx

##### Assigning G as the name of the graph we will make

G = nx.Graph()

####### Vertices #######

##Creating a single Node

G.add_node("Michael")

## Adding a list of Nodes

G.add_nodes_from([2,3])

####### Edges #######

## Adding edges and edge labels 

G.add_edge("Michael",2, film = "film 1")
G.add_edge(2,3, film = "film 2")
G.add_edge(3,"Michael", film = "film 3")




####### Drawing the graph #######

## Importing the package
import matplotlib.pyplot as plt

## Adding positions for each of the vertices:
pos = nx.spring_layout(G)
#pos = nx.circular_layout(G)
#pos = nx.random_layout(G)


########## Ways to draw a graph ##########

## To draw a simple graph with only the node and vertices use draw()
nx.draw(G)
#nx.draw_random(G)
#nx.draw_circular(G)
#nx.draw_spectral(G)


#### To add nodes and edges seperatley

## To draw just the vertices and edges only
#nx.draw_networkx(G)

## To print just the nodes on the graph use draw_networkx_nodes()
#nx.draw_networkx_nodes(G,pos)

## To print the node labels on graph draw_networkx_labels()
#nx.draw_networkx_labels(G,pos)

## To print just the edges on the graph use draw_networkx_nodes()
#nx.draw_networkx_edges(G,pos)

## To draw the graph with the node names use draw_networkx_edge_labels()
#nx.draw_networkx_edge_labels(G,pos)


## To print your graph to file:
#plt.savefig("U:\graph.png")

plt.show()
