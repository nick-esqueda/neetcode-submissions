class Solution:
    def climbStairs(self, n: int) -> int:
        """
        n is the number of steps to the top of the stairs (length of stairs?)


        n = 3
        1 + 1 + 1 = 3
        1 + 2 = 3
        2 + 1 = 3

                 __
              __|  |
            __|    |
          __|      |
        __|        |
       |       i  n |  

        n = numWays(n - 1) + numWays(n - 2)

        Qs:
        Isn't there overlap between ways to get to n-1 and n-2?
        - I guess that's the repeated work/subproblems?
        - But shouldn't those not be counted?
            - No, because they're parts of a "unique way" to get to N. It still counts
        """

        
        memo = {}
        def dfs(n):
            if n <= 2:
                return n
            if n in memo:
                return memo[n]

            memo[n] = dfs(n - 1) + dfs(n - 2)
            return memo[n]
    
        return dfs(n)