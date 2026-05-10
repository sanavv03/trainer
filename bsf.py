# graph = {
# # 0 spaces
#     'A': ['C', 'B'],
# # 4 spaces
#     'B': ['D', 'E'],
#     'C': ['F'],
#     'D': [],
#     'E': ['F'],
#     'F': []
# }

# def bfs(start_node, graph):
# # 0 spaces

#     visited = []
# # 4 spaces

#     queue = [start_node]
# # 4 spaces

#     while queue:
# # 4 spaces

#         node = queue.pop(0)
# # 8 spaces

#         if node not in visited:
# # 8 spaces

#             visited.append(node)
# # 12 spaces

#             neighbours = graph[node]
# # 12 spaces

#             queue.extend(neighbours)
# # 12 spaces

#     return visited
#     print("script is working")
# # 4 spaces

bsf():

graph = {
# 0 spaces
    'A': ['C', 'B'],
# 4 spaces
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

