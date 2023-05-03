# Band Festivities

**CISC320 Spring 2023 Lesson 14 - Graph Applications**

Group Members:
* Mikaylla Haskins (mikahas@udel.edu)
* Jillian Camp (jillsue@udel.edu)
* Grace O'Leary (goleary@udel.edu)

It's a band festival! There are bands playing at a local park, however no band can play directly beside another band, otherwise it'd be too noisy and hard to listen to each individual band's music! Therefore, a float must be placed inbetween each band so that way their music doesn't clash with eachother! Band 1 must also find the shortest path to get to Band 22.

## Installation Code

```sh
$> pip install networkx
import matplotlib.pyplot as plt
```

## Python Environment Setup

```python
import networkx as nx
import random
```

# Band 1 to Band 22

**Get Shortest Path From Band 1 to Band 22**: 

> **Formal Description**:
>  * Input: 
>  * Output: Final graph showcasing shortest path

**Graph Problem/Algorithm**: [DFS/BFS/SSSP/APSP/(MST)]


**Setup code**:

# Create an empty graph

```python

G = nx.Graph()

# Add 22 nodes to the graph
G.add_nodes_from(range(1, 23))

# Add edges between each node and every other node with random weights
for i in range(1, 23):
    for j in range(i + 1, 23):
        weight = random.randint(1, 10)  # Generate a random weight between 1 and 10
        G.add_edge(i, j, weight=weight)  # Add the edge with the generated weight

# Add edge between last and first node to create a loop with a random weight
weight = random.randint(1, 10)  # Generate a random weight between 1 and 10
G.add_edge(22, 1, weight=weight)  # Add the edge with the generated weight

# Print the graph information
print(nx.info(G))
```

**Visualization**:

![Image goes here](Relative image filename goes here)

**Solution code:**

```python


pos = nx.circular_layout(G)

# Get the weights of the edges
weights = [G[u][v]['weight'] for u,v in G.edges()]

# Draw the nodes and edges of the graph
nx.draw_networkx_nodes(G, pos, node_color='lightblue')
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edges(G, pos, width=weights)

# Show the graph
plt.axis('off')
plt.show()
nx.draw(G)


```

**Output**

```
plt.axis('off')
plt.show()
nx.draw(G)


```

**Interpretation of Results**:



# Is the parade too noisy? (Graph coloring)


