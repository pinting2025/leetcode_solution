# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return 0
            
            return 1 + max(dfs(node.left), dfs(node.right))
        
        max_depth = dfs(root)
        
        def find(node, lev):
            if not node:
                return 
            
            if lev == max_depth:
                return node
            
            left = find(node.left, lev+1)
            right = find(node.right, lev+1)
        
            if left and right:
                return node
            
            return left if left else right
        
        return find(root, 1)