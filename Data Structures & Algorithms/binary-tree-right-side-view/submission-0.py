# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        The last node in each level
        """
        if root is None:
            return []
        
        ans = list()
        q = deque([root])
        while len(q):
            last = 0
            for i in range(len(q)):
                node = q.popleft()
                last = node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(last)
        return ans