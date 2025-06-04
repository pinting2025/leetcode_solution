# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return
            
            if node.val == val:
                return node
            
            # return dfs(node.left) if dfs(node.left) else dfs(node.right)

            if val < node.val:
                return dfs(node.left)

            else:
                return dfs(node.right)
        
        return dfs(root)
            
        