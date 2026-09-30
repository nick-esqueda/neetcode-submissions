# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        smallest = None
        counter = 0
        def dfs(node):
            nonlocal counter, smallest
 
            if not node:
                return
            
            dfs(node.left)
 
            if counter == k:
                return
 
            counter += 1
            if counter == k:
                smallest = node.val
                return

            dfs(node.right)
 
        dfs(root)
        return smallest