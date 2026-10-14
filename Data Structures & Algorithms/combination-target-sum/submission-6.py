class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        allCombos = []
        def backtrack(start, combo, remaining):
            if remaining == 0:
                allCombos.append(combo.copy())
                return

            for i in range(start, len(nums)):
                if nums[i] > remaining:
                    return
                combo.append(nums[i])
                backtrack(i, combo, remaining - nums[i])
                combo.pop()
        
        backtrack(0, [], target)
        return allCombos
