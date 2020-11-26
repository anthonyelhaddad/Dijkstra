#Dijkstra BandWidth

import networkx as nx
import matplotlib.pyplot as plt
from numpy import *

def Dijkstra_BW(G,s):
    dist={}
    pred={}
    for i in G.nodes():
        dist[i]=0
        pred[i]=s

    dist[s]=inf
    X=list(G.nodes())

    while X:
        i=max(X, key=dist.get)

        for j in G.neighbors(i):
            if dist[j] < min(dist[i], G[i][j]['BW']):
                dist[j] = min(dist[i], G[i][j]['BW'])
                pred[j]=i
        X.remove(i)

    return dist, pred


wG=nx.read_edgelist('./BW.txt',nodetype=int,data=(('BW',int),))
[d, p] = Dijkstra_BW(wG, 0)
print(d)
print(p)
