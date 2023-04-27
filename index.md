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
```

## Python Environment Setup

```python
import networkx as nx
```

# Band 1 to Band 22

**Get Shortest Path From Band 1 to Band 22**: 

> **Formal Description**:
>  * Input: 
>  * Output: Final graph showcasing shortest path

**Graph Problem/Algorithm**: [DFS/BFS/SSSP/APSP/(MST)]


**Setup code**:

G = nx.Graph()

# Add 22 nodes to the graph
G.add_nodes_from(range(1, 23))

# Add edges between each node and every other node
for i in range(1, 23):
    for j in range(i + 1, 23):
        G.add_edge(i, j)

# Add edge between last and first node to create a loop
G.add_edge(22, 1)

# Print the graph information
print(nx.info(G))


// Create nodes:
G=nx.Graph()
H=nx.path_graph(22)
G.add_nodes_from(H)
G.add_node(H)

//Create edges:
G.add_edge(1,2)
e=(2,3)
G.add_edge(*e)
G.add_edges_from([(1,2),(1,3)])
```python
```

**Visualization**:

![Image goes here](Relative image filename goes here)

**Solution code:**

```python
```

**Output**

```
```

**Interpretation of Results**:

