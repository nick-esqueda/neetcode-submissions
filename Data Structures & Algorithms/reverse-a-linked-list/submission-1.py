# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        3     
        0 <- 1 <- 2 <- 3 -> N
   p    c 
        """
        
        def reverse(head, prev):
            if head is None:
                return prev
            newHead = reverse(head.next, head)
            head.next = prev
            return newHead

        return reverse(head, None)