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
import random
import matplotlib.pyplot as plt
```

# Band a to Band v

**Minimum spanning tree from band a to band v**: 

> **Formal Description**:
>  * Input: 
>  * Output: Final graph showcasing shortest path

**Graph Problem/Algorithm**: [DFS/BFS/SSSP/APSP/(MST)]


**Setup code**:

# Create an empty graph

```python

G = nx.Graph()

# Add nodes with labels A to V
for i in range(65, 87):
    G.add_node(chr(i))

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

# Define edge labels
edge_labels = nx.get_edge_attributes(G, 'weight')
```

**Visualization**:

![startinggraph.png](Relative image filename goes here)

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

> **Formal Description**:
>  * Input: A graph.
>  * Output: A boolean telling whether or not the graph is bipartite (two-colorable).

**Setup code**

# Create an empty graph

```python

# Create an empty graph

```python

G = nx.Graph()


# Print the graph information
print(nx.info(G))
# Call the function that executes the algorithm on this graph, G. 
print(is_bipartite(G))
```

**Visualization**:
![Image goes here](Figure_1.png)

**solution code** 
```python

def is_bipartite(graph):
    """
    Returns True if the given graph is bipartite, and False otherwise.
    """
    # Start DFS from an arbitrary node in the graph
    start_node = next(iter(graph.nodes()))
    visited = {start_node: 0}  # mark the start node as visited and assign it to set 0
    stack = [start_node]

    # Perform DFS while maintaining the visited set and the set assignments
    while stack:
        node = stack.pop()
        node_set = visited[node]

        # Assign the opposite color to all unvisited neighbors
        for neighbor in graph.neighbors(node):
            if neighbor not in visited:
                visited[neighbor] = 1 - node_set
                stack.append(neighbor)
            elif visited[neighbor] == node_set:
                # If a neighbor has the same color as the current node, the graph is not bipartite
                return False

    # If we've visited all nodes without conflicts, the graph is bipartite
    return True
```
**Output**

```python 
True 
```

**Interpretation of results**
