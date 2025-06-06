# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # return p == q, not correct since we're not checking if two treenode are pointing to the same memory

        queue1 = deque([p])
        queue2 = deque([q])

        while queue1 and queue2:
            length1 = len(queue1)
            length2 = len(queue2)
            if length1 != length2:
                return False

            for _ in range(length1):
                cur1 = queue1.pop()
                cur2 = queue2.pop()

                if not cur1 and not cur2:
                    continue
                
                if not cur1 or not cur2:
                    return False

                if cur1.val != cur2.val:
                    return False
                
                queue1.append(cur1.left)
                queue2.append(cur2.left)
                queue1.append(cur1.right)
                queue2.append(cur2.right)
        
        if queue1 or queue2:
            return False
            
        return True


