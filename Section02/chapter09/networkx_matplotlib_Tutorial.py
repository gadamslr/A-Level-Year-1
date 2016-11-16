# Creating a Graph

import networkx as nx

# assigning G as the name of the graph we will make

G = nx.Graph()

# Creating a single Node

G.add_node("Michael")
G.node["Michael"]["state"] = "Film1"

# Adding a list of Nodes

G.add_nodes_from([2,3])

# Adding edges of Nodes

G.add_edge("Michael",2, film = "film 1")
G.add_edge(2,3, film = "film 2")
G.add_edge(3,"Michael", film = "film 3")

#Adding positions for each of the vertices:
#pos = nx.circular_layout(G)
pos = nx.spring_layout(G)
#pos = nx.random_layout(G)

import matplotlib.pyplot as plt

# To draw the graph with the node and vertices use draw()
#nx.draw(G)
#nx.draw_random(G)
#nx.draw_circular(G)
#nx.draw_spectral(G)


#####To add 
# To print just the nodes on the graph use draw_networkx_nodes()
nx.draw_networkx_nodes(G,pos)
# To print the node labels on graph draw_networkx_labels()
nx.draw_networkx_labels(G,pos)

# To print just the edges on the graph use draw_networkx_nodes()
nx.draw_networkx_edges(G,pos)
# To draw the graph with the node names use draw_networkx_edge_labels()
nx.draw_networkx_edge_labels(G,pos)


plt.show()
#plt.savefig("D:\Long Road\Resources\Graphs\path.png")



