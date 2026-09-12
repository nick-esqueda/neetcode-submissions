# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        pQueue = deque([p])
        qQueue = deque([q])
        while len(pQueue) and len(qQueue):
            for i in range(len(pQueue)):
                pNode = pQueue.popleft()
                qNode = qQueue.popleft()

                if pNode is None and qNode is None:
                    continue
 
                if (pNode is None and qNode is not None
                    or qNode is None and pNode is not None):
                    return False
                
                if pNode.val != qNode.val:
                    return False
                
                pQueue.append(pNode.left)
                pQueue.append(pNode.right)
                qQueue.append(qNode.left)
                qQueue.append(qNode.right)

        return not len(pQueue) and not len(qQueue)