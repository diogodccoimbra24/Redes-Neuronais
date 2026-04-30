
import networkx as nx
import pandas as pd
from load_graph import load_graph
from plots import draw_graph
from metrics import degree_calc, in_degree_calc, out_degree_calc, betweenness_calc, closeness_calc, clustering_calc, density_calc, global_efficiency_calc, largest_scc_calc


#Path to the .edge file
path = "../data/macaque.edges"

#Directed graph for metrics
G = load_graph(path)


#Function used to draw the graph
draw_graph(G)

#Metrics
degree = degree_calc(G)
in_degree = in_degree_calc(G)
out_degree = out_degree_calc(G)
betweenness_c = betweenness_calc(G)
closeness = closeness_calc(G)
clustering = clustering_calc(G)

data = []

#Goes through every node and creates a list of dicts
for node in nx.nodes(G):
    data.append({

        "node": node,
        "degree": degree[node],
        "in_degree": in_degree[node],
        "out_degree": out_degree[node],
        "betweenness": betweenness_c[node],
        "closeness": closeness[node],
        "clustering": clustering[node]
    })

#Creation of the csv file with the result of the metrics
df = pd.DataFrame(data)
df.to_csv("../results/metrics_results.csv", index=False)


#Global metrics
density = density_calc(G)
global_e = global_efficiency_calc(G)
largest_scc = largest_scc_calc(G)


global_data = [{

        "density": density,
        "global_efficiency": global_e,
        "largest_scc": largest_scc
}]

#Creation of the csv file with the result of the global metrics
df_global = pd.DataFrame(global_data)
df_global.to_csv("../results/global_metrics_results.csv", index=False)






