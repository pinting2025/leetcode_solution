# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        def check(node, current_sum):
            if not node:
                return 0
            
            current_sum += node.val

            temp = 1 if current_sum == targetSum else 0
                
            return temp + check(node.left, current_sum) + check(node.right, current_sum)
        
        def dfs(node):
            if not node:
                return 0

            return check(node, 0) + dfs(node.left) + dfs(node.right)
        
        return dfs(root)

        



            




