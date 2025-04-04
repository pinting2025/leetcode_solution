# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(root):
            if not root:
                return 0
            
            left = dfs(root.left) + 1
            right = dfs(root.right) + 1

            return max(left, right)
        
        max_dep = dfs(root)
        
        def find(root, cur_dep):
            if not root:
                return (None, 0)
            
            if not root.left and not root.right:
                return (root,1) if cur_dep == max_dep else (None,0)

            left, left_count = find(root.left, cur_dep+1)
            right, right_count = find(root.right, cur_dep+1)

            if left_count > 0 and right_count > 0:
                return root, left_count + right_count
            
            if left_count > 0:
                return left, left_count

            if right_count > 0:
                return right, right_count

            return None, 0

        res, _ = find(root, 1)
        return res
            
            


        