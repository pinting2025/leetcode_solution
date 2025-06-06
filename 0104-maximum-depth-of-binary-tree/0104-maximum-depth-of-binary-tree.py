# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        # # bfs
        # queue = deque([root])
        # level = 0

        # while queue:
        #     level += 1
        #     length = len(queue)

        #     for _ in range(length):
        #         current = queue.popleft()
        #         if current.left:
        #             queue.append(current.left)
        #         if current.right:
        #             queue.append(current.right)
        
        # return level

        # dfs
        res = 0
        def dfs(node, depth):
            nonlocal res
            if not node:
                return 
            
            if not node.left and not node.right:
                res = max(res, depth)
            
            if node.left:
                dfs(node.left, depth+1)
            if node.right:
                dfs(node.right, depth+1)
            
            return
        
        dfs(root, 1)

        return res

            