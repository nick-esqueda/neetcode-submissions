import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # Put all into a heap
        heapq.heapify(nums)
 
        # len(nums) - k times, pop from heap (leaving k nums)
        for _ in range(len(nums) - k):
            heapq.heappop(nums)

        # Now, heap has only the k largest nums with the min of those at top
        self.kLargestHeap = nums
        self.k = k

    def add(self, val: int) -> int:
        if len(self.kLargestHeap) < self.k:
            heapq.heappush(self.kLargestHeap, val)
            return self.kLargestHeap[0]
 
        if val > self.kLargestHeap[0]:
            heapq.heapreplace(self.kLargestHeap, val)
        return self.kLargestHeap[0]
        
