# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        q1 = [p]
        q2 = [q]
        while len(q1) and len(q2):
            q1Node = q1.pop()
            q2Node = q2.pop()

            if (q1Node is None and q2Node is not None
                or q2Node is None and q1Node is not None):
                return False
            
            if q1Node is None and q2Node is None:
                continue

            if (q1Node.val != q2Node.val):
                return False
            
            q1.append(q1Node.left)
            q1.append(q1Node.right)
            q2.append(q2Node.left)
            q2.append(q2Node.right)
            
        return not len(q1) and not len(q2)