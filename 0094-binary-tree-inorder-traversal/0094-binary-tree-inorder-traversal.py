# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        # left, middle, right
        def inorder(node):
            if not node:
                return 

            # go to the left
            inorder(node.left)

            # current 
            res.append(node.val)

            # go to the right
            inorder(node.right)

            return 
        
        inorder(root)

        return res