

import networkx as nx
import matplotlib.pyplot as plt


#Representation of the graph
def draw_graph(G):

    #Calculates the position of the nodes, seed = 42 to keep the graph always the same
    pos = nx.spring_layout(G, seed=42)

    nx.draw_networkx_nodes(G, pos, node_size=50)
    nx.draw_networkx_edges(G, pos, arrows=False, alpha=0.05)

    plt.axis("off")
    plt.show()