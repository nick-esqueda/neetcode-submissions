import heapq
from math import sqrt

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for x, y in points:
            distance = sqrt(x**2 + y**2)
            heapq.heappush(minHeap, (distance, (x, y)))

        result = []
        for _ in range(k):
            distance, point = heapq.heappop(minHeap)
            result.append(point)
        
        return result
