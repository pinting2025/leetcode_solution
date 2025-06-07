# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, mini, maxi):
            if not node:
                return True
            
            if node.left:
                if node.left.val <= mini or node.left.val >= node.val:
                    return False    
            
            if node.right:
                if node.right.val >= maxi or node.right.val <= node.val:
                    return False
            
            return dfs(node.left, mini, node.val) and dfs(node.right, node.val, maxi)
        
        return dfs(root, float('-inf'), float('inf'))
            
        
            

                