import matplotlib.pyplot as plt

import networkx as nx

G=nx.Graph()
Tree=nx.Graph()

G.add_edge(1,2)
G.add_edge(1,8)
G.add_edge(2,3)
G.add_edge(2,8)
G.add_edge(3,4)
G.add_edge(3,8)
G.add_edge(4,7)
G.add_edge(4,9)
G.add_edge(5,6)
G.add_edge(5,7)
G.add_edge(7,8)


def bfs_fired(G, start, fired):
    Q=[start]
    fired.add(start)
    while len(Q)!=0:
        current= Q.pop(0)
        for neighbour in G[current]:
            if neighbour not in fired:
                fired.add(neighbour)
                Tree.add_edge(current, neighbour)
                Q.append(neighbour)

fired=set()
bfs_fired(G,  6, fired)
nx.draw_spectral(Tree)
plt.show()
