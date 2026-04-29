
import networkx as nx
from load_graph import load_graph
from plots import draw_graph

#Path to the .edge file
path = "../data/macaque.edges"

G = load_graph(path)


#Variables to indicate the number of nodes, edges and if it's directional
nodes = nx.number_of_nodes(G)
edges = nx.number_of_edges(G)
directed = nx.is_directed(G)

print(f"Number of nodes: {nodes}")
print(f"Number of edges: {edges}")
print(f"Is directed: {directed}")

#Function used to draw the graph
draw_graph(G)


