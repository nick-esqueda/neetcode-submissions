class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        can't have duplicates (same freq of each num)

        take this one, vs.
        skip this one and move on?
        """

        result = []
        def dfs(i, combo, comboSum):
            if comboSum == target:
                result.append(combo.copy())
            if i >= len(nums) or comboSum >= target:
                return

            # Take
            combo.append(nums[i])
            dfs(i, combo, comboSum + nums[i])

            # Skip
            combo.pop()
            dfs(i + 1, combo, comboSum)
        
        dfs(0, [], 0)
        return result