# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        """

        dummy = ListNode(0, None)
        curr = dummy
        next1 = list1
        next2 = list2

        while (next1 is not None) or (next2 is not None):
            if next2 is None:
                curr.next = next1
                curr = next1
                next1 = next1.next
            elif next1 is None:
                curr.next = next2
                curr = next2
                next2 = next2.next
            elif next1.val <= next2.val:
                curr.next = next1
                curr = next1
                next1 = next1.next
            else:
                curr.next = next2
                curr = next2
                next2 = next2.next

        return dummy.next