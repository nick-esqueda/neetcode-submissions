from functools import cache
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def backtrack(amount):
            if amount == 0:
                return 0

            minCoins = float('inf')
            for coin in coins:
                if amount - coin >= 0:
                    minCoins = min(minCoins, 1 + backtrack(amount - coin))

            return minCoins

        minCoins = backtrack(amount)
        return minCoins if minCoins != float('inf') else -1
 