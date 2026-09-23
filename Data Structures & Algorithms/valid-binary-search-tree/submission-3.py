# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        need to check ALL vals in L subtree are < node, same for R
        if all L < node and all R > node, and both L & R are BSTs, current is valid BST
        pass down 
        """

        flattened = list()

        def dfs(root):
            if not root:
                return
            
            dfs(root.left)
            flattened.append(root.val)
            dfs(root.right)

        dfs(root)

        for i in range(1, len(flattened)):
            if flattened[i - 1] >= flattened[i]:
                return False
        return True

