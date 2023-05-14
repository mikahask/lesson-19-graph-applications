from matplotlib import pyplot as plt
import networkx as nx

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
                print(stack)
            elif visited[neighbor] == node_set:
                # If a neighbor has the same color as the current node, the graph is not bipartite
                return False

    # If we've visited all nodes without conflicts, the graph is bipartite
    return True
G = nx.Graph()
G.add_nodes_from(range(20))
for i in range(20):
    for j in range(i+1, 20):
        G.add_edge(i, j)
pos = {i: (i % 10, i // 10) if i < 10 else ((i-10) % 10, (i-10) // 10 + 1) for i in range(20)}
nx.draw(G, pos=pos, with_labels=True)    
#plt.show() # show the plot

# Check if the graph is bipartite
print(is_bipartite(G))

