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

        originalToCopy = dict()
        copyToOriginal = dict()

        def copyList(node):
            if not node:
                return None

            nextCopy = copyList(node.next)

            copyNode = Node(node.val, nextCopy)
            originalToCopy[node] = copyNode
            copyToOriginal[copyNode] = node
            return copyNode
        copy = copyList(head)

        curr = copy
        while curr:
            original = copyToOriginal[curr]
            if original.random:
                randomCopy = originalToCopy[original.random]
                curr.random = randomCopy
            curr = curr.next
        
        return copy
        