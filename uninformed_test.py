import networkx as nx
import matplotlib.pyplot as plt
from bfs import bfs
from dfs import dfs
from id_dfs import iddfs

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}

G = nx.DiGraph()

for node, neighbors in graph.items():
    for neighbor in neighbors:
        G.add_edge(node, neighbor)

pos = {
    'A': (2, 4),
    'B': (1, 3),
    'C': (3, 3),
    'D': (0.5, 2),
    'E': (1.5, 2),
    'F': (3, 2),
    'G': (1.5, 1)
}

plt.figure(figsize=(6, 5))

nx.draw(
    G, pos,
    with_labels=True,
    node_color='lightblue',
    node_size=2000,
    font_size=12,
    font_weight='bold',
    arrows=True,
    arrowsize=15,
    edge_color='black'
)

plt.title("Graph Representation")
plt.axis('off')
plt.show()

print("BFS:", bfs(graph, 'A'))
print("DFS:", dfs(graph, 'A'))
print("IDDFS:", iddfs(graph, 'A', 3))