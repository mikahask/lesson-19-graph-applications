import networkx as nx
import matplotlib.pyplot as plt

import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

# Add nodes with labels A to V
for i in range(65, 87):
    G.add_node(''+ chr(i))

# Add edges to the graph
G.add_edge('A', 'F', weight=7)
G.add_edge('A', 'D', weight=5)
G.add_edge('B', 'C', weight=8)
G.add_edge('B', 'F', weight=9)
G.add_edge('B', 'E', weight=7)
G.add_edge('C', 'G', weight=5)
G.add_edge('D', 'F', weight=6)
G.add_edge('D', 'E', weight=15)
G.add_edge('E', 'F', weight=8)
G.add_edge('E', 'J', weight=9)
G.add_edge('F', 'G', weight=11)
G.add_edge('F', 'H', weight=8)
G.add_edge('G', 'I', weight=9)
G.add_edge('H', 'I', weight=7)
G.add_edge('H', 'L', weight=5)
G.add_edge('I', 'J', weight=6)
G.add_edge('I', 'L', weight=12)
G.add_edge('J', 'K', weight=10)
G.add_edge('K', 'L', weight=6)
G.add_edge('L', 'M', weight=8)
G.add_edge('M', 'N', weight=9)
G.add_edge('M', 'O', weight=10)
G.add_edge('N', 'P', weight=6)
G.add_edge('O', 'P', weight=7)
G.add_edge('O', 'S', weight=5)
G.add_edge('P', 'Q', weight=4)
G.add_edge('Q', 'R', weight=6)
G.add_edge('R', 'V', weight=9)
G.add_edge('S', 'T', weight=5)
G.add_edge('T', 'U', weight=7)
G.add_edge('U', 'V', weight=8)
G.add_edge('B', 'D', weight=3)
G.add_edge('C', 'F', weight=7)
G.add_edge('G', 'H', weight=5)
G.add_edge('I', 'K', weight=10)
G.add_edge('J', 'L', weight=4)
G.add_edge('M', 'R', weight=12)
G.add_edge('N', 'S', weight=8)
G.add_edge('O', 'T', weight=6)
G.add_edge('P', 'U', weight=9)
G.add_edge('Q', 'V', weight=11)
G.add_edge('L', 'S', weight=7)
G.add_edge('L', 'V', weight=10)
G.add_edge('L', 'A', weight=8)
G.add_edge('L', 'B', weight=9)
G.add_edge('A', 'G', weight=6)
G.add_edge('B', 'D', weight=10)
G.add_edge('C', 'H', weight=7)
G.add_edge('D', 'J', weight=8)
G.add_edge('E', 'K', weight=12)
G.add_edge('F', 'M', weight=13)
G.add_edge('G', 'N', weight=9)
G.add_edge('H', 'O', weight=11)
G.add_edge('I', 'P', weight=7)
G.add_edge('J', 'Q', weight=5)
G.add_edge('K', 'R', weight=9)
G.add_edge('L', 'S', weight=7)
G.add_edge('M', 'T', weight=6)
G.add_edge('N', 'U', weight=8)
G.add_edge('O', 'V', weight=10)

# Define edge labels
edge_labels = nx.get_edge_attributes(G, 'weight')

# Compute the minimum spanning tree from node A to V
T = nx.algorithms.tree.minimum_spanning_tree(G.subgraph(nx.node_connected_component(G, 'A')), weight='weight')

# Draw the graph and tree
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, node_color='lightblue')
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edges(G, pos)
nx.draw_networkx_edges(T, pos, edge_color='red', width=2)
# plt.axis('off')
plt.show()

# plt.axis('off')
# plt.show()
# nx.draw(G)