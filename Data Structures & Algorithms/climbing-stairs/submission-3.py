class Solution:
    def climbStairs(self, n: int) -> int:
        """
                 __
              __|  |
            __|    |
          __|      |
        __|        |
       | i       n |  

        n = numWays(n - 1) + numWays(n - 2)
        """
        
        if n <= 2:
            return n

        dp = [0] * n
        dp[0] = 1
        dp[1] = 2

        for i in range(2, len(dp)):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[-1]
