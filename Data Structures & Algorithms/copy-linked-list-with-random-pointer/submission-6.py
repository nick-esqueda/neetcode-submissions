"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCopy = { None: None }
 
        def copy(node):
            if not node:
                return None

            oldToCopy[node] = Node(node.val)
 
            tail = copy(node.next)
            copyNode = oldToCopy[node]
            copyNode.next = tail
            copyNode.random = oldToCopy[node.random]
            return copyNode
        
        return copy(head)
        