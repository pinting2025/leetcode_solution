# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # right, middle, left, start from most right
        total = 0

        def sum_up(node):
            nonlocal total
            if not node:
                return 
            
            # go to the right node
            sum_up(node.right)

            # update current node value
            total += node.val
            node.val = total

            # go to the left node
            sum_up(node.left)
        
        sum_up(root)

        return root






            
            
            



