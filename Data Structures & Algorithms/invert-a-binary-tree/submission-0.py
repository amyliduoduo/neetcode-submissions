# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #BFS: process the tree level by level (for each node, swap its children, then push the children into the queue)

        if not root:
            return None
        
        queue = deque([root]) #initialize queue by pushing the root node

        while queue:
            node = queue.popleft() #remove the front/root node from the queue
            node.left, node.right = node.right, node.left #swap its left and right children
            #then add the new left and right children into the queue
            if node.left:
                 queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return root #return the root as the inverted tree