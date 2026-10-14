class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        allCombos = []
        def backtrack(i, combo, remaining):
            if remaining == 0:
                allCombos.append(combo.copy())
                return
            if i >= len(nums):
                return

            for j in range(i, len(nums)):
                if remaining - nums[j] < 0:
                    break
                combo.append(nums[j])
                backtrack(j, combo, remaining - nums[j])
                combo.pop()
        
        backtrack(0, [], target)
        return allCombos
