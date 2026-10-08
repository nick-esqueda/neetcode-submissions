class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        can't have duplicates (same freq of each num)

        take this one, vs.
        skip this one and move on?
        """

        result = []
        combo = []
        comboSum = 0
        def dfs(i):
            nonlocal comboSum
 
            if comboSum == target:
                result.append(combo.copy())
            if i >= len(nums) or comboSum >= target:
                return

            # Take
            combo.append(nums[i])
            comboSum += nums[i]
            dfs(i)

            # Skip
            combo.pop()
            comboSum -= nums[i]
            dfs(i + 1)
        
        dfs(0)
        return result