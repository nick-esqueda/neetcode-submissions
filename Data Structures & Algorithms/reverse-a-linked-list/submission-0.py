# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
     <- 0 <- 1 <- 2 <- 3  null
                       p   tc          

        3.next = the previous node?

        """

        curr = head
        prev = None
        while curr is not None:
            temp = curr.next
            curr.next = prev

            prev = curr
            curr = temp
        
        return prev