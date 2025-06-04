# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def dfs(node, key):
            if not node:
                return None

            if node.val > key:
                node.left = dfs(node.left, key)

            elif node.val < key:
                node.right = dfs(node.right, key)

            else:
                # no child
                if not node.left and not node.right:
                    return None
                # only one child
                elif not node.left:
                    return node.right
                elif not node.right:
                    return node.left
                # two child, get the smallest one on the right side
                else:
                    min_node = findmin(node.right)
                    node.val = min_node.val
                    node.right = dfs(node.right, min_node.val)
            
            return node
            
        def findmin(node):
            while node.left:
                node = node.left
            return node
        
        return dfs(root, key)

            
            