# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        res = None

        def is_node(node):
            nonlocal res
            if not node:
                return 0

            left = is_node(node.left)
            right = is_node(node.right)

            cur = 1 if (node == p or node == q) else 0

            if left + right + cur >= 2:
                res = node
            
            return 1 if (left or right or cur) else 0

        is_node(root)

        return res
