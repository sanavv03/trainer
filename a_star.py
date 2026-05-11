import heapq

def astar(grid, start, goal):
    # Dimensions of the grid
    rows, cols = len(grid), len(grid[0])
    
    # Priority Queue (Open List): stores (f_score, current_node)
    # We start with the start node. f = g + h. 
    # At start, g=0, so f = h.
    open_list = []
    heapq.heappush(open_list, (0, start))
    
    # Dictionary to track the movement cost from start to a node (g_score)
    g_score = {start: 0}
    
    # Dictionary to store the path (who is the parent of this node?)
    came_from = {}

    while open_list:
        # 1. Pick the node with the lowest F-score
        current_f, current = heapq.heappop(open_list)

        # 2. Check if we reached the goal
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            return path[::-1] # Return reversed path

        # 3. Check neighbors (Up, Down, Left, Right)
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            neighbor = (current[0] + dx, current[1] + dy)

            # Is neighbor inside the grid and not a wall?
            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols:
                if grid[neighbor[0]][neighbor[1]] == 1:
                    continue # It's a wall

                # Calculate tentative G-score (cost to reach neighbor)
                tentative_g = g_score[current] + 1
                
                # If this path is better than any previous one
                if neighbor not in g_score or tentative_g < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    
                    # H-score: Manhattan Distance (Distance if there were no walls)
                    h_score = abs(neighbor[0] - goal[0]) + abs(neighbor[1] - goal[1])
                    f_score = tentative_g + h_score
                    
                    heapq.heappush(open_list, (f_score, neighbor))

    return None # No path found

# --- Example Usage ---
# 0 = Path, 1 = Wall
maze = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0]
]

start_pos = (0, 0)
goal_pos = (3, 4)

result = astar(maze, start_pos, goal_pos)
print(f"Path from {start_pos} to {goal_pos}:")
print(result)

























# [START]
#   |
#   v
# [Put Start Node in OPEN List]
#   |
#   v
# <---[Is OPEN List empty?]---> (YES) ---> [No Path Found]
#   | (NO)
#   v
# [Pick node with lowest F-score] 
# [This is the "Current Node"]
#   |
#   v
# <---[Is it the Goal?]---> (YES) ---> [Success! Path Found]
#   | (NO)
#   v
# [Move Current Node to CLOSED List]
#   |
#   v
# [Look at all Neighbors]
#   |
#   +--[Is Neighbor a wall/closed?]---> (YES) ---> [Ignore]
#   |
#   +--[Is Neighbor new?]--------------> (YES) ---> [Calc F-score & add to OPEN]
#   |
#   +--[Is path to Neighbor cheaper?]--> (YES) ---> [Update Neighbor's F-score]
#   |
#   v
# [Back to "Is OPEN List empty?"]


