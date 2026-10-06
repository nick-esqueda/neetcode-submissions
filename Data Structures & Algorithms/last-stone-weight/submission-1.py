import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        
        while len(stones) > 1:
            stone1 = -(heapq.heappop(stones))
            stone2 = -(heapq.heappop(stones))
            remaining = max(stone1, stone2) - min(stone1, stone2)

            if remaining:
                heapq.heappush(stones, -remaining)
        
        return -(stones[0]) if stones else 0