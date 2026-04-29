

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


