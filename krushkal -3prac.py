# Disjoint Set (Union-Find) Class:
# This structure manages groups of vertices to efficiently detect cycles.
class DisjointSet:
    def __init__(self, vertices):
        # self.parent: Initially, every vertex is its own parent (its own "set").
        self.parent = {v: v for v in vertices}
        # self.rank: Used to keep the tree flat; height is 0 for all nodes initially.
        self.rank = {v: 0 for v in vertices}

    def find(self, vertex):
        # find(): Recursively finds the root/representative of the set containing 'vertex'.
        if self.parent[vertex] != vertex:
            # Path compression: Makes future lookups faster by pointing node directly to the root.
            self.parent[vertex] = self.find(self.parent[vertex])
        return self.parent[vertex]

    def union(self, v1, v2):
        # union(): Merges two separate sets into one.
        root1 = self.find(v1)
        root2 = self.find(v2)

        # Only merge if the vertices belong to different roots (sets).
        if root1 != root2:
            # Union by rank: Attach the shorter tree under the taller tree to maintain efficiency.
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            elif self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            else:
                # If ranks are equal, pick one as root and increment its rank.
                self.parent[root2] = root1
                self.rank[root1] += 1

# Kruskal's Algorithm Function:
# Finds the Minimum Spanning Tree (MST) of a graph.
def kruskal_mst(vertices, edges):
    # 1. Sort edges by weight (the 3rd element in the tuple) in ascending order.
    # This is the "Greedy" step: always consider the cheapest edges first.
    edges = sorted(edges, key=lambda x: x[2])
    
    # 2. Initialize the Disjoint Set with the provided vertices.
    ds = DisjointSet(vertices)
    
    # 3. mst: List to store final edges; total_weight: Sum of weights in the MST.
    mst = []
    total_weight = 0

    # 4. Iterate through each edge in the sorted list.
    for u, v, weight in edges:
        # Check for cycle: If find(u) and find(v) are different, they are not connected.
        if ds.find(u) != ds.find(v):
            # No cycle detected, so merge the sets.
            ds.union(u, v)
            # Add the edge to our MST list.
            mst.append((u, v, weight))
            # Update the cumulative weight.
            total_weight += weight
            # Print the selected edge as the algorithm runs.
            print(f"Selected Edge: ({u}, {v}, {weight})")

    # 5. Return the completed MST and the final weight sum.
    return mst, total_weight

# --- Example Graph Setup (as per your notebook) ---
vertices = ['A', 'B', 'C', 'D']

edges = [
    ('A', 'B', 1),
    ('A', 'C', 3),
    ('B', 'C', 2),
    ('B', 'D', 4),
    ('C', 'D', 5)
]

# --- Execution ---
mst, weight = kruskal_mst(vertices, edges)

# --- Final Output ---
print("\nMinimum Spanning Tree:", mst)
print("Total Weight of MST:", weight)