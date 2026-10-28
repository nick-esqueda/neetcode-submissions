# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Alternating & moving inward
        Head, tail, head, tail, head, tail
        Reverse the last half of the list, then merge with first half?
        When merging, iterate until len/2 
        Edge case: odds/evens

        [0, 1, 2 ,3, 4, 5, 6]
        [6, 5, 4, 3, 2, 1, 0]
        """

        fwd = []
        listLen = 0
        curr = head
        while curr:
            listLen += 1
            fwd.append(curr)
            curr = curr.next
        rev = list(reversed(fwd))

        for node in fwd:
            node.next = None

        dummy = ListNode()
        curr = dummy
        i = 0
        while i < (listLen // 2):
            curr.next = fwd[i]
            curr = curr.next
            curr.next = rev[i]
            curr = curr.next
            i += 1
        
        if len(fwd) % 2 == 1:
            curr.next = fwd[i]
