# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #DFS the entire tree and collect all node values
        arr = []

        def dfs(node):
            if not node:
                return None
            
            arr.append(node.val)
            dfs(node.left)
            dfs(node.right)
        
        dfs(root) #starts the traversal process by invoking dfs on the tree's root node, populating arr with all values in the tree.

        #sort the collected values
        arr.sort()

        #The k-th smallest element is at index k-1 in the sorted list.
        return arr[k - 1]

