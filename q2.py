#!/usr/bin/python
# -*- coding: utf-8 -*-
#Importing the queue into the codes 
from queue import Queue

#Initializing the graph arrary
graph = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['a'],
    'd': ['e'],
    'e': ['d'],
    'f': [],
    }
#Decraling and list the Node which has been visited 
Nodesv = {}  
#Initialize a queue
queue = Queue()   
level = {}
parent = {}
bfs_output = []
weight = 4
#Staring the for look of the graph
for node in graph.keys():
    Nodesv[node] = False
    parent[node] = None
    level[node] = -1

s = 'a'

Nodesv[s] = True

level[s] = 0

queue.put(s)

while not queue.empty():
    u = queue.get()
    bfs_output.append(u)

    for v in graph[u]:
        if not Nodesv[v]:
            Nodesv[v] = True
            parent[v] = u
            level[v] = level[u] + 1

            queue.put(v)
#Using the for loop in the codes 
            for w in level:
                dist = weight * level[v]
                #Prinring the distanec from a node to another 
            print (
                'The Distance from',
                s,
                'to',
                v,
                'is',
                dist,
                )
#Printing the Traversed nodes in the bfs order
print ('BFS traversed nodes in this order: ', bfs_output)
