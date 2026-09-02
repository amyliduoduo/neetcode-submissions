# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #Recursion

        #edge case: no root no p and no q
        if not root or not p or not q:
            return None
        
        #both values less than current node ---- left subtree
        if max(p.val, q.val) < root.val:
            #move on to left child by recursively calling its method
            return self.lowestCommonAncestor(root.left, p, q)
        
        elif min(p.val, q.val) > root.val:
            return self.lowestCommonAncestor(root.right, p, q)

        #one less one greater, then current node is LCA
        else:
            return root