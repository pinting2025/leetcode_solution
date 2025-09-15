# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # either use count variable to count kth smallest node we are on or triverse through all nodes and store them in a list
        res = []

        def inorder(node):
            if not node:
                return 
            
            inorder(node.left)
            res.append(node.val)
            inorder(node.right)
        
            return 

        inorder(root)

        return res[k-1]

        
        