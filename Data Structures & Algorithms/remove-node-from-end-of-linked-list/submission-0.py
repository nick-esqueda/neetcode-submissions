# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def remove(node, prev):
            if node is None:
                return 1
            
            countFromEnd = remove(node.next, node)

            if countFromEnd == n:
                prev.next = node.next
    
            return countFromEnd + 1
        
        dummy = ListNode()
        dummy.next = head
        remove(head, dummy)
        return dummy.next