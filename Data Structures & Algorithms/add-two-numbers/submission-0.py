# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
             1    1    1
        7 -> 8 -> 9 -> n
        7 -> 8 -> 9 -> n
        4    7    9    1

        res: 1 -> 5 -> 7 -> 8 -> n

        if you have a carry at the very end (root), need to make a dummy node
        """

        nodes = []
        carry = 0
        curr1, curr2 = l1, l2
        while curr1 or curr2:
            currSum = carry
            if curr1:
                currSum += curr1.val
                curr1 = curr1.next
            if curr2:
                currSum += curr2.val
                curr2 = curr2.next

            if currSum > 9:
                carry = 1
                currSum -= 10
            else:
                carry = 0
            
            nodes.append(ListNode(currSum))

        if carry:
            nodes.append(ListNode(1))
        
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]

        return nodes[0]