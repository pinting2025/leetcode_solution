# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = deque([root])
        ans = float('-inf')
        max_lev = 0
        temp = 0
        cur_lev = 1

        while queue:
            lev_len = len(queue)
            while lev_len > 0:
                cur = queue.popleft()
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
                temp += cur.val
                lev_len -= 1

            if temp > ans:
                ans = temp
                max_lev = cur_lev

            cur_lev += 1
            temp = 0
        
        return max_lev






        
            

        