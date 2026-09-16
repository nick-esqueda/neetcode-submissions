# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        make 2 separate lists, one with nodes forward, one backward?
        [ 0, 1, 2, 3, 4, 5, 6 ]
          i
        
        [                     ]

        forward and backwards will always be the same length
        """

        forward, backward = list(), list()

        def dfs(node):
            if node is None:
                return None
            
            forward.append(node)
            dfs(node.next)
            backward.append(node)
            node.next = None
        dfs(head)

        dummy = ListNode()
        curr = dummy
        i = 0
        while i < (len(forward) // 2):
            curr.next = forward[i]
            curr = curr.next
 
            curr.next = backward[i]
            curr = curr.next
            i += 1
        
        if len(forward) % 2 == 1:
            curr.next = forward[i]
