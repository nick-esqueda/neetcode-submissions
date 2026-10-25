class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Recursive top-down DP
        Make sure to pull answers up instead of send down
        """

        memo = {}
        def dfs(i):
            if i == 0:
                return nums[0]
            if i == 1:
                return max(nums[0], nums[1])
            if i in memo:
                return memo[i]
            
            maxMoney = max(
                nums[i] + dfs(i - 2),  # Take
                dfs(i - 1)             # Skip
            )

            memo[i] = maxMoney
            return memo[i]
        
        return dfs(len(nums) - 1)
        