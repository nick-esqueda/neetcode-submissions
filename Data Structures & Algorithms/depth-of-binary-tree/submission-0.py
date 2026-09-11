# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        as you recurse down, how do you know how deep you are?
        pass depth itself into subtrees when recursing so each node knows it's depth
        """
        ans = float('-inf')
        def dfs(root, currDepth):
            nonlocal ans
 
            if root is None:
                return

            ans = max(ans, currDepth)
            dfs(root.left, currDepth + 1)
            dfs(root.right, currDepth + 1)
            return
        
        dfs(root, 1)
        return 0 if ans == float('-inf') else ans

        