

import networkx as nx


def load_graph(path):

    #Function used to read the .edge file and builds a directed graph
    G = nx.read_edgelist(path,
                         create_using=nx.DiGraph(),
                         nodetype=int)

    return G


