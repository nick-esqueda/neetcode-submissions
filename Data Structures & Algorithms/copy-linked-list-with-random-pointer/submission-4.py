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
        """
             |---------|
        3 -> 7 -> 4 -> 5 -> null
        ^ --------|
 
        iter through LL, make copy LL
        put nodes to copyNodes map? or list?
        iter through copyList (to set next pointers)
        get the copy
        """
        if not head:
            return None

        oldToCopy = dict()
        def copyList(node):
            if not node:
                return None

            nextCopy = copyList(node.next)

            copyNode = Node(node.val, nextCopy)
            oldToCopy[node] = copyNode
            return copyNode
        copy = copyList(head)

        curr = head
        while curr:
            copy = oldToCopy[curr]
            if curr.random:
                copy.random = oldToCopy[curr.random]
            curr = curr.next
        
        return oldToCopy[head]
        