"""
A graph is a collection of nodes (or vertices) and edges that connect pairs of nodes.
 Graphs can be directed or undirected, weighted or unweighted.

Graphs can be represented using an adjacency list or an adjacency matrix.
"""

# USing Adjacency List

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def print_graph(self):
        for node in self.graph:
            print(f"{node}: {self.graph[node]}")

# Example usage
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.print_graph()
# Output:
# 0: [1, 2]
# 1: [2]
# 2: [0, 3]

# Adjacency Matrix
"""
    0
   / \
  1---2
   \
    3
Here,
Vertex 0 is connected to vertices 1 and 2.
Vertex 1 is connected to vertices 0, 2, and 3.
Vertex 2 is connected to vertices 0 and 1.
Vertex 3 is connected to vertex 1.



    0  1  2  3
0 [ 0, 1, 1, 0 ]
1 [ 1, 0, 1, 1 ]
2 [ 1, 1, 0, 0 ]
3 [ 0, 1, 0, 0 ]

"""

"""
class Graph:
    def __init__(self, vertices):
        self.V = vertices  # Number of vertices
        self.adj_matrix = [[0] * vertices for _ in range(vertices)]  # Initialize the adjacency matrix

    def add_edge(self, u, v):
        # Since the graph is undirected, we add edges in both directions
        self.adj_matrix[u][v] = 1
        self.adj_matrix[v][u] = 1

    def print_graph(self):
        for row in self.adj_matrix:
            print(row)

# Example usage
g = Graph(4)  # Create a graph with 4 vertices
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(1, 3)

g.print_graph()
# Output:
# [0, 1, 1, 0]
# [1, 0, 1, 1]
# [1, 1, 0, 0]
# [0, 1, 0, 0]

"""


# Graphs are versatile structures that can represent complex relationships and networks.
# They can be directed or undirected and can be weighted or unweighted.

# The adjacency matrix is a straightforward way to represent graphs, especially when the graph is dense (i.e., has many edges).
# However, it can consume more memory compared to an adjacency list for sparse graphs (i.e., graphs with relatively few edges).