# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #DFS
        #For the root, the allowed range is (-∞, +∞)
        #For BST, the entire left branch is less than the parent, (left, node.val)
        #For BST, the entire right branch is greater than the parent, (node.val, right)

        #go down the tree, tighten the bounds
        
        #helper function that uses recursive DFS
        def valid(node, left, right):
        #edge case: empty subtree is BST
            if not node:
                return True
            #check if the node falls in the range
            if not (left < node.val < right):
                return False
            
            return valid(node.left, left, node.val) and valid(node.right, node.val, right)


        return valid(root, float("-inf"), float("inf"))
        


