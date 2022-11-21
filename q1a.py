#!/usr/bin/python
# -*- coding: utf-8 -*-
# Import the main file from the main folder to be used in the codes

from common import *

# Importing network

import networkx as nx
import matplotlib.pyplot as plt     

#Function k_mst_edges 

def k_mst_edges(
    G,
    minimum,
    weight='weight',
    keys=True,
    data=True,
    ):
    subtrees = UnionFind()
    #Starting the if condition
    if G.is_multigraph():
        edges = G.edges(keys=True, data=True)
    else:
        edges = G.edges(data=True)
    #Intializing the function getweight
    def getweight(t):
        return t[-1].get(weight, 1)

    edges = sorted(edges, key=getweight, reverse=not minimum)
    is_multigraph = G.is_multigraph()

    # Multigraphs need to handle edge keys in addition to edge data.

    if is_multigraph:
        for (u, v, k, d) in edges:
            if subtrees[u] != subtrees[v]:
                if keys:
                    if data:
                        yield (u, v, k, d)
                    else:
                        yield (u, v, k)
                else:
                    if data:
                        yield (u, v, d)
                    else:
                        yield (u, v)
                subtrees.union(u, v)
    else:
        for (u, v, d) in edges:
            if subtrees[u] != subtrees[v]:
                if data:
                    yield (u, v, d)
                else:
                    yield (u, v)
                subtrees.union(u, v)


# parameters
# G - graph
# minimum - True if minimum spanning tree, False if maximum spanning tree
# weight - edge attribute to use as weight
# keys - True if edge keys are to be included in the output
# data - True if edge data is to be included in the output

# sample usage

G = nx.Graph()
G.add_edge('a', 'c', weight=8)
G.add_edge('a', 'f', weight=5)
G.add_edge('a', 'l', weight=14)
G.add_edge('f', 'i', weight=8)
G.add_edge('f', 'k', weight=16)
G.add_edge('f', 'b', weight=20)
G.add_edge('f', 'd', weight=94)
G.add_edge('k', 'b', weight=47)
G.add_edge('k', 'j', weight=5)
G.add_edge('b', 'h', weight=12)
G.add_edge('b', 'd', weight=8)
G.add_edge('g', 'j', weight=5)
G.add_edge('g', 'l', weight=13)
G.add_edge('g', 'c', weight=12)
G.add_edge('l', 'e', weight=15)
G.add_edge('l', 'h', weight=14)

#Now here we about to print the minimum spanning tree with the corresponding codes
print ('Minimum spanning tree:')
for edge in k_mst_edges(G, True):
    print (edge)

plt.show()