class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        Base case: 
        Starting at 0 or 1 means you pay cost[0/1] and that's it
        """

        dp = [0] * len(cost)
        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, len(dp)):
            # Each idx holds the min cost to get there, + the cost to move to next step
            dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])
        
        return min(dp[-1], dp[-2])