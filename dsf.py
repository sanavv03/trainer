# The Graph: Represented as an adjacency list
# Each key is a node, and the value is a list of its connected neighbors
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

def perform_dfs(graph, start):
    """Function to perform Depth First Search traversal"""
    
    # 1. 'visited' stores the nodes in the order we discover them
    visited = [] 
    
    # 2. 'stack' keeps track of nodes to explore next (Last-In, First-Out)
    stack = [start] 

    # 3. Loop continues until there are no more nodes left in the stack
    while stack:
        
        # 4. Remove the last element added to the stack (the 'top' plate)
        current_node = stack.pop() 
        
        # 5. Only process the node if it hasn't been visited yet
        if current_node not in visited:
            
            # 6. Mark the node as visited by adding it to our list
            visited.append(current_node)
            
            # 7. Get the neighbors of the current node from the dictionary
            neighbors = graph[current_node]
            
            # 8. Add neighbors to the stack to explore them in the next iterations
            # We use reversed() so the first neighbor stays on top of the stack
            stack.extend(reversed(neighbors))
            
    # 9. Return the final list showing the DFS traversal path
    return visited

# --- Execution ---
# Call the function and store the result
result = perform_dfs(graph, 'A')

# Print the final path to the console
print("DFS Path:", result)