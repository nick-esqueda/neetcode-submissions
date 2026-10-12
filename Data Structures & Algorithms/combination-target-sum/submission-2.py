class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        allCombos = []
        def backtrack(i, combo, comboSum):
            if comboSum == target:
                allCombos.append(combo.copy())
            if comboSum >= target or i >= len(nums):
                return
            
            # Take num
            combo.append(nums[i])
            backtrack(i, combo, comboSum + nums[i])

            # Skip num
            combo.pop()
            backtrack(i + 1, combo, comboSum)
        
        backtrack(0, [], 0)
        return allCombos
