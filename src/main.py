
import networkx as nx
import pandas as pd
from load_graph import load_graph
from plots import draw_graph
from metrics import degree_calc

#Path to the .edge file
path = "../data/macaque.edges"
G = load_graph(path)

#Function used to draw the graph
draw_graph(G)

#Function used calculate the degree of each node
degree = degree_calc(G)

data = []

#Goes through every node and creates a list of dicts
for node in nx.nodes(G):
    data.append({
        "node": node,
        "degree": degree[node]
    })

#Creation of the csv file with the result of the metrics
df = pd.DataFrame(data)
df.to_csv("../results/metrics_results.csv", index=False)





