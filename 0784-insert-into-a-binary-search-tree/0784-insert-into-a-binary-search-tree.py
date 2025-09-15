# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            root = TreeNode()
            root.val = val
            return root

        def search(node):
            if not node:
                return 

            if val > node.val:
                # if no right child, insert
                if not node.right:
                    node.right = TreeNode()
                    node.right.val = val
                    return 
                # move to the right side
                else:
                    search(node.right)
            
            else:
                # if no left child, insert
                if not node.left:
                    node.left = TreeNode()
                    node.left.val = val
                    return 
                # move to the left
                else:
                    search(node.left)
            return 

        search(root)

        return root