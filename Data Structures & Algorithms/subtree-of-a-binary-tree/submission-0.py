# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #edge cases: either tree or subtree is empty
        if not subRoot:
            return True
        if not root:
            return False

        #go through each node in DFS and check if the subtree starting here is exactly the same as subRoot
        if self.sameTree(root, subRoot):
            return True
        #if the roots didn't match, search deeper further with the left branch
        elif self.isSubtree(root.left, subRoot):
            return True
        #else search deeper further with the right branch
        else:
            return self.isSubtree(root.right, subRoot)

    #define sameTree method (root1, root2)
    def sameTree(self, root, subRoot):
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        if root.val != subRoot.val:
            return False
        return self.sameTree(root.left, subRoot.left) and self.sameTree(root.right, subRoot.right) #recursively check left children and right children



