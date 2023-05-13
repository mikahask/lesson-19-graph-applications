# Band Festivities

**CISC320 Spring 2023 Lesson 14 - Graph Applications**

Group Members:
* Mikaylla Haskins (mikahas@udel.edu)
* Jillian Camp (jillsue@udel.edu)
* Grace O'Leary (goleary@udel.edu)

It's a band festival! There are bands playing at a local park! Each band is named after the alphabet from letters a to v. To get the fullest experience, we've created a map which showcases routes between bands which will allow you to travel to each band within optimal time!

## Installation Code

```sh
$> pip install networkx
import matplotlib.pyplot as plt
import startinggraph.png
```

## Python Environment Setup

```python
import networkx as nx
import matplotlib.pyplot as plt
```

# Band a to Band v

**Minimum spanning tree from band a to band v**: 

> **Formal Description**:
>  * Input: Band Festival Map
>  * Output: Final graph showcasing Minimum Spanning Tree of Band Festival Map

**Graph Problem/Algorithm**: [DFS/BFS/SSSP/APSP/(MST)]


**Setup code**:

# Create an empty graph

```python

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
```

**Visualization**:

![startinggraph.png](Relative image filename goes here)

**Solution code:**

```python

# Compute the minimum spanning tree from node A to V
T = nx.algorithms.tree.minimum_spanning_tree(G.subgraph(nx.node_connected_component(G, 'Band A')), weight='weight')

# Draw the graph and tree
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, node_color='lightblue')
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edges(G, pos)
nx.draw_networkx_edges(T, pos, edge_color='red', width=2)

```

**Output**

```python
# plot graph
plt.show()


```

**Interpretation of Results**:
These results indicate the optimal routes from each band to get from one band to another with the shortest amount of distance as possible. This graph has accomplished the goal of a minimum spanning tree.
