# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []

        def dfs(node, current_sum, path):
            nonlocal res
            if not node:
                return 0
            
            path = path + [node.val] # should create a new copy of the path list, or else they'll all be store in a same list
            
            if not node.left and not node.right:
                if current_sum + node.val == targetSum:
                    res.append(path)
                    return 

            dfs(node.left, current_sum + node.val, path)
            dfs(node.right, current_sum + node.val, path)
        
        dfs(root, 0, [])

        return res


