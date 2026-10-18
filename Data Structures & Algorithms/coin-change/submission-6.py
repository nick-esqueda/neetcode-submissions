class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # CAN YOU NOT DO 'USED' ARCHITECTURE?
            # You want to RETURN used, not take it in.
        # Have to return 0 - base case is different?
        # Maybe the 2 structures ask different "questions"
        # What are you wanting DP to hold in the other style?

        # If it uses the whole array, isn't it not take/skip?

        # Top-down DP really doesn't fit as well as iterative??
        # How is this 1D-DP and not 2D?


        dp = {} # Stores ans (min coins) for a given amount. (Given the whole array)
        def backtrack(remaining): # Returns the ans - min num coins to hit target
            if remaining in dp:
                return dp[remaining]
            if remaining == 0:
                return 0

            minCoins = float('inf')
            for coin in coins:
                if remaining - coin >= 0:
                    newMin = 1 + backtrack(remaining - coin)
                    minCoins = min(minCoins, newMin)

            dp[remaining] = minCoins
            return dp[remaining]
            
        minCoins = backtrack(amount)
        return minCoins if minCoins != float('inf') else -1