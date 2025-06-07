# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # find root.val == subroot.val
        target = subRoot.val
        res = False

        def is_valid(root, subRoot):
            if not root and not subRoot:
                return True
            if not root or not subRoot:
                return False
            if root.val != subRoot.val:
                return False
            
            return is_valid(root.left, subRoot.left) and is_valid(root.right, subRoot.right)

        def dfs(node):
            nonlocal res
            if not node:
                return False
            
            if node.val == target:
                res = is_valid(node, subRoot)
                if res == True:
                    return True
            
            return dfs(node.left) or dfs(node.right) or res

        return dfs(root)
        
