# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        temp = root.left
        root.left = root.right
        """

        def invert(curr):
            if curr is None:
                return None

            invert(curr.left)
            invert(curr.right)

            temp = curr.left
            curr.left = curr.right
            curr.right = temp
            return curr
        
        return invert(root)
        