# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        The node has to be greater than everything that came before it

               3
            3
          4   2
        """
        
        count = 0
        def dfs(root, maxInPath):
            nonlocal count
            if root is None:
                return

            if root.val >= maxInPath:
                count += 1
                maxInPath = root.val
 
            dfs(root.left, maxInPath)
            dfs(root.right, maxInPath)
        
        dfs(root, float('-inf'))
        return count