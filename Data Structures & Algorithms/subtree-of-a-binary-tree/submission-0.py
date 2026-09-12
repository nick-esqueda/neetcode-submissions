# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        traverse through tree
        if subroot val matches curr val, perform dfs to check if is subtree
        otherwise, keep traversing
        keep going b/c might be another val that matches subRoot elsewhere in tree
        visited set useful here?
        """

        def areTreesEqual(root1, root2):
            if root1 is None and root2 is None:
                return True 
            if (root1 is None and root2 is not None
                or root2 is None and root1 is not None):
                return False
            if root1.val != root2.val:
                return False
            
            isLeftEqual = areTreesEqual(root1.left, root2.left)
            isRightEqual = areTreesEqual(root1.right, root2.right)
            return isLeftEqual and isRightEqual

        def hasSubtreeMatch(root, subRoot):
            if root is None:
                return False
            
            if areTreesEqual(root, subRoot):
                return True

            leftHasMatch = hasSubtreeMatch(root.left, subRoot)
            rightHasMatch = hasSubtreeMatch(root.right, subRoot)
            return leftHasMatch or rightHasMatch
        
        return hasSubtreeMatch(root, subRoot)
