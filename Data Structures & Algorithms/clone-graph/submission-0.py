"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #DFS
        
        #create a hashmap to store original nodes -> cloned nodes.
        oldToNew = {}

        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]
            #clone a new node with the same value
            copy = Node(node.val)
            #store it in the map
            oldToNew[node] = copy #key-value assignment where key is the node and value is the copy
            #
            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))
            return copy

        return dfs(node) if node else None       
