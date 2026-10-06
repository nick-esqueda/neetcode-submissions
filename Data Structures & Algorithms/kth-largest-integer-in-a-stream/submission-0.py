import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        heap = [-n for n in nums]
        heapq.heapify(heap)
        self.maxHeap = heap
        self.k = k

    def add(self, val: int) -> int:
        heapq.heappush(self.maxHeap, -val)

        popped = []
        for i in range(self.k):
            num = -(heapq.heappop(self.maxHeap))
            popped.append(num)
 
        kthLargest = popped[-1]

        for num in popped:
            heapq.heappush(self.maxHeap, -num)

        return kthLargest
        
