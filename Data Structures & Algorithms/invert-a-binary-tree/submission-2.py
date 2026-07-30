# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #DFS: use recursion to invert subtrees in a top-down manner

        if not root:
            return None
        
        #swap left and right children
        root.left, root.right = root.right, root.left

        #recursively call DFS on the new left and right children
        self.invertTree(root.left) #self represents the instance of the class that is currently calling the method
        self.invertTree(root.right)

        return root