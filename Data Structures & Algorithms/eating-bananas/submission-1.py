from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        Want the slowest speed k that allows you to eat all bananas within h hours
        Slower speed, longer time, less bananas
        Faster speed, less time, more bananas

        [F,F,F,T,T,T]
        k = [1, 2, 3, ..., max(piles)]
        timeTaken = [10h, 8h, 6h, 4h, ..., len(piles)]
        """

        def canFinish(k):
            totalTime = 0
            for pile in piles:
                totalTime += ceil(pile / k)
            return totalTime <= h

        lo, hi = 1, max(piles)
        while lo < hi:
            mid = lo + (hi - lo) // 2

            if canFinish(mid):
                hi = mid
            else:
                lo = mid + 1

        return lo