# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        res = 1
        cur_level = 1
        max_sum = float('-inf')

        queue = deque([root])

        while queue:
            length = len(queue)
            temp = 0

            for _ in range(length):
                current = queue.popleft()
                temp += current.val
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            
            if temp > max_sum:
                res = cur_level
                max_sum = temp
            
            cur_level += 1
        
        return res






