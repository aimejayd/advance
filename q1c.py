
from heapq import heappop, heappush
from itertools import count


import networkx as nx

# Define the function edges to be used 
def prim_mst_edges(G, minimum, weight='weight', keys=True, data=True):
    is_multigraph = G.is_multigraph()
    push = heappush
    pop = heappop
# Nodes List
    nodes = list(G)
    c = count()

    sign = 1
    if not minimum:
        sign = -1

    while nodes:
        u = nodes.pop(0)
        frontier = []
        visited = [u]
        if is_multigraph:
            for u, v, k, d in G.edges(u, keys=True, data=True):
                push(frontier, (d.get(weight, 1) * sign, next(c), u, v, k))
        else:
            for u, v, d in G.edges(u, data=True):
                push(frontier, (d.get(weight, 1) * sign, next(c), u, v))
        while frontier:
            if is_multigraph:
                W, _, u, v, k = pop(frontier)
            else:
                W, _, u, v = pop(frontier)
            if v in visited:
                continue
            visited.append(v)
            nodes.remove(v)
            if is_multigraph:
                for _, w, k2, d2 in G.edges(v, keys=True, data=True):
                    if w in visited:
                        continue
                    new_weight = d2.get(weight, 1) * sign
                    push(frontier, (new_weight, next(c), v, w, k2))
            else:
                for _, w, d2 in G.edges(v, data=True):
                    if w in visited:
                        continue
                    new_weight = d2.get(weight, 1) * sign
                    push(frontier, (new_weight, next(c), v, w))
            # Multigraphs need to handle edge keys in addition to edge data.
            if is_multigraph and keys:
                if data:
                    yield u, v, k, G[u][v]
                else:
                    yield u, v, k
            else:
                if data:
                    yield u, v, G[u][v]
                else:
                    yield u, v


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


for u, v, d in prim_mst_edges(G, True, 'weight', True, True):
    print(f"({u}, {v}, " + str(d) + ")")
