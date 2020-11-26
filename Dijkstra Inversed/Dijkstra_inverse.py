# Dijkstra Inversed

import networkx as nx
import matplotlib.pyplot as plt
from numpy import *


wG=nx.read_edgelist('./graph.txt',create_using=nx.DiGraph(),nodetype=str,data=(('weight',double),))
#print(wG['H1']['1']['weight'])
#print(nx.dijkstra_path(wG,'H1','V'))
#print(nx.dijkstra_path_length(wG,'H1','V'))


def Dijkstra_inverse(G,s):
    dist={}
    pred={}
    for i in G.nodes():
        dist[i]=inf
        pred[i]=s

    dist[s]=0
    X=list(G.nodes())

    while X:
        i=min(X, key=dist.get)

        for j in G.predecessors(i):
            if dist[j] > dist[i] + G[j][i]['weight']:
                dist[j] = dist[i] + G[j][i]['weight']
                pred[j]=i
        X.remove(i)

    return dist, pred



[p,q]=Dijkstra_inverse(wG, "V")
print(p)
print(q)
