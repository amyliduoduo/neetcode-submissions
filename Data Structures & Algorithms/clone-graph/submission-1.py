"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #Hashmap + DFS

        #hashmap to store visited to avoid duplicates
        oldToNew = {} #key is the original node, value is the cloned node

        #DFS: recursively clones its neighbors, and returns the cloned node
        def dfs(node):
            #base case
            if node in oldToNew:
                return oldToNew[node]
            else:
                clone = Node(node.val) #clone it
                oldToNew[node] = clone #store in hashmap
            
            #Recursively clone all neighbors and add them to the clone’s neighbor list.
            for neighbor in node.neighbors:
                clone.neighbors.append(dfs(neighbor))
            return clone

        #edge case
        if node is not None:
            return dfs(node)
        else:
            return None
            

        