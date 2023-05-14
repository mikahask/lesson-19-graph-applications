import networkx as nx
import matplotlib.pyplot as plt

# Create an empty graph
G = nx.Graph()

# Add 20 nodes
G.add_nodes_from(range(20))

# Add 35 edges to make the graph denser
G.add_edges_from([(0,1),(1,2),(2,3),(3,4),(4,5),(5,6),(6,7),(7,8),(8,9),(9,10),(10,11),(11,12),(12,13),(13,14),(14,15),(15,16),(16,17),(17,18),(18,19),(0,3),(3,6),(6,9),(9,12),(12,15),(15,18),(1,4),(4,7),(7,10),(10,13),(13,16),(16,19),(0,2),(2,4),(4,6),(6,8),(8,10),(10,12)])

# Label every other node as "band" or "float"
node_labels = {}
for node in G.nodes():
    if node % 2 == 0:
        node_labels[node] = "band"
    else:
        node_labels[node] = "float"

# Set the node labels as an attribute of the graph
nx.set_node_attributes(G, node_labels, "label")

# Separate the nodes into two sets based on their labels
bands = {n for n,attrdict in G.nodes(data=True) if attrdict['label']=='band'}
floats = set(G) - bands

# Create a bipartite graph with the two node sets
B = nx.Graph()
B.add_nodes_from(bands, bipartite=0)
B.add_nodes_from(floats, bipartite=1)
B.add_edges_from(G.edges())

# Draw the graph with a spring layout and save it as a PNG image
pos = nx.spring_layout(B)
nx.draw(B, pos=pos, with_labels=True)
node_labels = nx.get_node_attributes(B, 'label')
nx.draw_networkx_labels(B, pos, labels=node_labels)
plt.savefig('bipartite_graph.png')
plt.show()