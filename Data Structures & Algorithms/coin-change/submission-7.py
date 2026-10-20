class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        """

        dp = {}
        def backtrack(amount):
            if amount == 0:
                return 0
            if amount in dp:
                return dp[amount]

            minCoins = float('inf')
            for coin in coins:
                if amount - coin >= 0:
                    minCoins = min(minCoins, 1 + backtrack(amount - coin))

            dp[amount] = minCoins
            return dp[amount]

        minCoins = backtrack(amount)
        return minCoins if minCoins != float('inf') else -1
