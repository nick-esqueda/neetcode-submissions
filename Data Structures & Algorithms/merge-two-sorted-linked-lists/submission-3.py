# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        curr, next1, next2 = dummy, list1, list2
        while next1 and next2:
            if next1.val < next2.val:
                curr.next = next1
                next1 = next1.next
            else:
                curr.next = next2
                next2 = next2.next
        
            curr = curr.next
        
        if next1:
            curr.next = next1
        else:
            curr.next = next2
        
        return dummy.next