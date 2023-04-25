import pandas as pd
from numpy import genfromtxt
import matplotlib.pyplot as plt
import networkx as nx


mydata = genfromtxt('file.txt', delimiter=' ')
G = nx.DiGraph(mydata)

print(G)
print(len(G.nodes), len(G.edges))

nx.draw(G, with_labels=True)

graph = G.degree
even_degree_vertices = []

for vertex in graph:
    if vertex[1] % 2 == 0:
        even_degree_vertices.append(vertex)

print(even_degree_vertices) 

#bubble sort
for i in range(len(even_degree_vertices)-1):
    for j in range(len(even_degree_vertices)-1-i):
        if even_degree_vertices[j][1] < even_degree_vertices[j+1][1]:
            even_degree_vertices[j], even_degree_vertices[j+1] = even_degree_vertices[j+1], even_degree_vertices[j]
            
            
print(even_degree_vertices)
