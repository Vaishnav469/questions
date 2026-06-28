"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldtonew = {}
        def dfs(node):
            if node in oldtonew:
                return oldtonew[node]
            copynode = Node(node.val)
            oldtonew[node] = copynode
            for neighbour in node.neighbors:
                copynode.neighbors.append(dfs(neighbour)) 
            return copynode
        return dfs(node) if node else None