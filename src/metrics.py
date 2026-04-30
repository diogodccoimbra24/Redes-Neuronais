

import networkx as nx


#Metrics

#Fuction used to calculate the degree of each node
def degree_calc(G):

    deg = dict(G.degree())
    return deg


#Function used to calculate the in degree of each node
def in_degree_calc(G):

    in_deg = dict(G.in_degree())
    return in_deg


#Function used to calculate the out degree of each node
def out_degree_calc(G):

    out_deg = dict(G.out_degree())
    return out_deg


#Function used to calculate the betweenness centrality of each node
def betweenness_calc(G):

    bet = nx.betweenness_centrality(G)
    return bet


#Function used to calculate the closeness centrality of each node
def closeness_calc(G):

    clo = nx.closeness_centrality(G)
    return clo


#Function used to calculate the clustering of each node
def clustering_calc(G):

    clustering = nx.clustering(G)
    return clustering


#Global metrics

#Function to calculate the density
def density_calc(G):

    density = nx.density(G)
    return density

#Function to calculate the global efficiency
def global_efficiency_calc(G):

    global_e = nx.global_efficiency(G.to_undirected())
    return global_e

#Function to calculate the size of the largest strongly connected component
def largest_scc_calc(G):

    scc = nx.strongly_connected_components(G)
    largest_scc = max(scc, key=len)
    return len(largest_scc)



