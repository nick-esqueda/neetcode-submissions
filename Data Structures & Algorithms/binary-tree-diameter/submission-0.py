# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        In other words, what's the max (ldepth + rdepth) in the tree?
        Need to return the current max depth AND the depth of self?
        """

        def getDiameter(root):
            if root is None:
                return (0, 0)
    
            lMax, lDepth = getDiameter(root.left)
            rMax, rDepth = getDiameter(root.right)

            lrMax = max(lMax, rMax) # 0
            currDepth = max(lDepth, rDepth) + 1 # 0
            currMax = max(lrMax, (lDepth + rDepth)) # 1

            return (currMax, currDepth) # 1, 1
            
        return getDiameter(root)[0]