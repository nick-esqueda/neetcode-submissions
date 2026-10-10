import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # """
        # Each list in sorted order already
        # You don't know how many lists you have till the start - need to be dynamic
        # Lists could be diff length

        # Maintain all nums so you know which one needs to go next?
        # Need access in increasing order

        # Each iteration, you compare all of the heads and take smallest

        # Need multiple pointers for .nexts - 1 per LL

        # how do you know (from min node map) which LL has that node?
        # take all curr nodes in currMap, in LL, find idx of smallest?
 
        # {
        #   0: node(4)
        #   1: node(3)
        #   2: node(3)
        # }

        #       1           2   ->   4   ->   n
        #     /   \      /  c       n0
        #   /       \   /                          
        # d           1        3   ->   5   ->   n
        #                      n1
                                                                                          
        #                   3   ->   6   ->   n
        #                   n2

        # curr = dummy
        # while:
        #     nextKey = getKeyOfMinNode() || 0
        #     curr.next = currMap[nextKey]
        #     currMap[nextKey] = currMap[nextKey].next
        #     curr = curr.next
        
        # getKeyOfMinNode():
        #     minKey = 
        #     minVal = 
        #     for node in currMap:
        #         if node is not none and node.val < minVal:
        #             minKey = node.key
        #             minVal = node.val
        #     return minKey
        
        # OPTIMIZATION:
        # Above solution is O(k*n) - iterating over all lists each time you set next node
        # Need faster
        # Can't iterate over all lists each time to find min
        # Need constant access to next min, so...
        # Use heap

        # Heap will store the head vals for each list
        # When need to find next min, use heap root
        # Replace heap root with the lists[nextIdx].next value for the next iter

        # BUT, if you cant put real node on heap, how do you know which LL the val belongs?
        # (val, nodeIdx)
        # """

        if not lists:
            return None

        headValueHeap = [] # (val, nodeIdx)
        for i, head in enumerate(lists):
            if head:
                headValueHeap.append((head.val, i))
        heapq.heapify(headValueHeap)

        dummy = ListNode()
        curr = dummy
        while curr and headValueHeap:
            nextVal, nextIdx = heapq.heappop(headValueHeap)
            curr.next = lists[nextIdx]
            curr = curr.next
 
            if lists[nextIdx] is not None:
                lists[nextIdx] = lists[nextIdx].next
                if lists[nextIdx] is not None:
                    heapq.heappush(headValueHeap, (lists[nextIdx].val, nextIdx))

        return dummy.next