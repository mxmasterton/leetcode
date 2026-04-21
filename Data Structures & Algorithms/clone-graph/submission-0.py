"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        old_to_new = {}

        visited = set()
        def dfs1(vertex):
            if vertex not in visited:
                visited.add(vertex)
                old_to_new[vertex] = Node(vertex.val)
                for neighbor in vertex.neighbors:
                    dfs1(neighbor)
        dfs1(node)

        visited = set()
        def dfs2(vertex):
            if vertex not in visited:
                visited.add(vertex)
                for neighbor in vertex.neighbors:
                    old_to_new[vertex].neighbors.append(old_to_new[neighbor])

                for neighbor in vertex.neighbors:
                    dfs2(neighbor)
        dfs2(node)

        return old_to_new[node]



