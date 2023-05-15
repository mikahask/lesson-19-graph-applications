import networkx as nx
import matplotlib.pyplot as plt
import random


def is_bipartite(graph):
    """
    Returns a message indicating whether the given graph is bipartite or not.
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
                return "The graph is not bipartite"

    # If we've visited all nodes without conflicts, the graph is bipartite
    return "The graph is bipartite"
# Set the number of nodes
num_nodes = 20


G = nx.Graph()

# Add two sets of nodes, each with num_nodes/2 vertices
G.add_nodes_from(range(num_nodes//2), bipartite=0)
G.add_nodes_from(range(num_nodes//2, num_nodes), bipartite=1)

edges = []
for i in range(num_nodes//2):
    neighbors = random.sample(range(num_nodes//2, num_nodes), random.randint(1, num_nodes//2-1))
    edges += [(i, j) for j in neighbors]
G.add_edges_from(edges)

# Assign a color to each node based on its bipartite set
color_map = ['red' if G.nodes[n]['bipartite'] == 0 else 'blue' for n in G.nodes()]

# Draw the bipartite graph with labels and colors using a spring layout
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, node_color=color_map)
print(is_bipartite(G))
