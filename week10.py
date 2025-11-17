# Global variables for timing and results
entry_time = {}
exit_time = {}
timer = 0
topo_stack = []


def DFS(G, v, marked):
    """Depth-first search on adjacency matrix."""
    global timer

    # Record entry time when vertex is first visited
    timer += 1
    entry_time[v] = timer

    # Mark the current vertex as visited
    marked.append(v)

    # Consider all neighbors of v
    for w in range(len(G)):
        # For any edge v --> w, if w is unmarked, visit it
        if G[v][w] != G[0][0] and w not in marked:
            DFS(G, w, marked)

    # Record exit time after exploring all neighbors
    timer += 1
    exit_time[v] = timer

    # Add vertex to topological stack
    topo_stack.append(v)
    return marked


def DFS_helper(G, v):
    """Helper method to launch a DFS from vertex v."""
    # Launch DFS from v with empty marked list
    return DFS(G, v, [])

def topological_sort(G):
    """Perform topological sort using recursive DFS."""
    marked = []
    for v in range(len(G)):
        if v not in marked:
            DFS(G, v, marked)
    topo_stack.reverse()
    return topo_stack






G = [
    [0, 1, 1, 0, 0, 0],  
    [0, 0, 0, 1, 0, 0],  
    [0, 0, 0, 1, 1, 0],  
    [0, 0, 0, 0, 0, 1],  
    [0, 0, 0, 0, 0, 1],  
    [0, 0, 0, 0, 0, 0]   
]


# Run topological sort
order = topological_sort(G)
print("Topological Sort Order:", order)


print("Entry times:", entry_time)
print("Exit times:", exit_time)


