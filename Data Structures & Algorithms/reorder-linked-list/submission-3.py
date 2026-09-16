# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """

        1 -> 2 -> 3 -> 4 -> n
             s         f
        """
        if not head or not head.next:
            return None

        # Step 1: Find middle node
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Step 2: Reverse the 2nd list
        curr = slow.next
        slow.next = None
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # Step 3: Merge the two lists
        dummy = ListNode()
        curr = dummy
        next1 = head
        next2 = prev
        while next1 and next2:
            curr.next = next1
            curr = curr.next
            next1 = next1.next
            curr.next = next2
            curr = curr.next
            next2 = next2.next
        
        curr.next = next1 if next1 else next2
