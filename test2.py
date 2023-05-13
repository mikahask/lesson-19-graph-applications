import networkx as nx
import matplotlib.pyplot as plt

# create the graph (same as before)
G = nx.Graph()
G.add_nodes_from(range(20))
for i in range(20):
    for j in range(i+1, 20):
        G.add_edge(i, j)

# arrange the nodes in two straight lines
pos = {i: (i % 10, i // 10) if i < 10 else ((i-10) % 10, (i-10) // 10 + 1) for i in range(20)}

nx.draw(G, pos=pos, with_labels=True) # draw the nodes and edges
plt.savefig("my_graph.png") # save the plot as a PNG file
plt.show() # show the plot (optional)