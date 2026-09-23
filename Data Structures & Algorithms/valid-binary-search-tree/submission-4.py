# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        if you go left, pass in updated upper bound of curr.val
        if you go right, pass in updated LOWER bound of curr.val (keep upper bound as curr parent)
        """

        def dfs(root, lower, upper):
            if not root:
                return True
            
            isCurrValid = (lower < root.val < upper)
            isLeftValid = dfs(root.left, lower, root.val)
            isRightValid = dfs(root.right, root.val, upper)

            return isCurrValid and isLeftValid and isRightValid
        
        return dfs(root, float('-inf'), float('inf'))
