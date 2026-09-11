# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def detectBalance(root):
            if root is None:
                return (True, 0)
            
            isLBalanced, lHeight = detectBalance(root.left)
            isRBalanced, rHeight = detectBalance(root.right)
 
            currHeight = max(lHeight, rHeight) + 1

            if (not isLBalanced 
                or not isRBalanced
                or abs(lHeight - rHeight) > 1):
                return (False, currHeight)
 
            return (True, currHeight)
        
        return detectBalance(root)[0]
            