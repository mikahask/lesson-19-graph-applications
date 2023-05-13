import networkx as nx
import matplotlib.pyplot as plt

import networkx as nx
import matplotlib.pyplot as plt

# Define the graph
G = nx.Graph()

# Add nodes with labels A to V
for i in range(65, 87):
    G.add_node('Band ' + chr(i))

# Add edges to the graph
G.add_edge('Band A', 'Band F', weight=7)
G.add_edge('Band A', 'Band D', weight=5)
G.add_edge('Band B', 'Band C', weight=8)
G.add_edge('Band B', 'BandF', weight=9)
G.add_edge('Band B', 'Band E', weight=7)
G.add_edge('Band C', 'Band G', weight=5)
G.add_edge('Band D', 'Band F', weight=6)
G.add_edge('Band D', 'Band E', weight=15)
G.add_edge('Band E', 'Band F', weight=8)
G.add_edge('Band E', 'Band J', weight=9)
G.add_edge('Band F', 'Band G', weight=11)
G.add_edge('Band F', 'Band H', weight=8)
G.add_edge('Band G', 'Band I', weight=9)
G.add_edge('Band H', 'Band I', weight=7)
G.add_edge('Band H', 'Band L', weight=5)
G.add_edge('Band I', 'Band J', weight=6)
G.add_edge('Band I', 'Band L', weight=12)
G.add_edge('Band J', 'Band K', weight=10)
G.add_edge('Band K', 'Band L', weight=6)
G.add_edge('Band L', 'Band M', weight=8)
G.add_edge('Band M', 'Band N', weight=9)
G.add_edge('Band M', 'Band O', weight=10)
G.add_edge('Band N', 'Band P', weight=6)
G.add_edge('Band O', 'Band P', weight=7)
G.add_edge('Band O', 'Band S', weight=5)
G.add_edge('Band P', 'Band Q', weight=4)
G.add_edge('Band Q', 'Band R', weight=6)
G.add_edge('Band R', 'Band V', weight=9)
G.add_edge('Band S', 'Band T', weight=5)
G.add_edge('Band T', 'Band U', weight=7)
G.add_edge('Band U', 'Band V', weight=8)

# Define edge labels
edge_labels = nx.get_edge_attributes(G, 'weight')

# Draw the graph
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True)
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.show()
# plt.axis('off')
nx.draw(G)