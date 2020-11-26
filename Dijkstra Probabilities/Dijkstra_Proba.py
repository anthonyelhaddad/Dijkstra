#Dijkstra Probabilities

import networkx as nx
import matplotlib.pyplot as plt
from numpy import *

def Dijkstra_Proba(G,s):
    dist={}
    pred={}
    for i in G.nodes():
        dist[i]=0
        pred[i]=s

    dist[s]=1
    X=list(G.nodes())

    while X:
        i=max(X, key=dist.get)

        for j in G.neighbors(i):
            if dist[j] < (dist[i] * G[i][j]['proba.txt']):
                dist[j] = dist[i] * G[i][j]['proba.txt']
                pred[j]=i
        X.remove(i)

    return dist, pred

wG=nx.read_edgelist('./proba.txt',nodetype=int,create_using=nx.DiGraph(),data=(('proba.txt',float),))
[d, p] = Dijkstra_Proba(wG, 1)
print(d)
print(p)
