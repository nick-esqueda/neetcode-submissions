from functools import lru_cache

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        min cost to hit the top of staircase (1 after last index)
        each step costs something to move past it

        Brute Force:
        calc cost of every possible combination of climbing the stairs
        maintain a min
        """

        @lru_cache
        def findCost(i):
            if i <= 1:
                return cost[i]
 
            cost1 = findCost(i - 1)
            cost2 = findCost(i - 2)
            currMin = min(cost1, cost2)

            return currMin if i >= len(cost) else currMin + cost[i]
        
        return findCost(len(cost))