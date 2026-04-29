

import networkx as nx

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

