"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        self.visited = {}
        return self.dfs(node)
    
    def dfs(self, curr):
        if curr.val in self.visited:
            return self.visited[curr.val]

        new_node = Node(curr.val)
        self.visited[curr.val] = new_node
        for next_node in curr.neighbors:
            new_node.neighbors.append(self.dfs(next_node))
        return new_node

            


