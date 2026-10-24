# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(node, prev):
            if not node:
                return prev

            newHead = reverse(node.next, node)
            node.next = prev
            return newHead

        return reverse(head, None)       
