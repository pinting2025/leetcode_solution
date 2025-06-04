# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # dfs 
        def dfs(node, current_sum):
            if not node:
                return False
            
            if not node.left and not node.right:
                if current_sum + node.val == targetSum:
                    return True

            left = dfs(node.left, current_sum + node.val)
            right = dfs(node.right, current_sum + node.val)

            return left or right
        
        return dfs(root, 0)
                


            

