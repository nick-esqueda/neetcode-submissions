class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        "Choosing any from this set of numbers"
        Add them together (curr level) in loop?
        Still need i to iter because you still need a way to "skip" nums
        """

        allCombos = []
        def backtrack(i, combo, comboSum):
            if comboSum == target:
                allCombos.append(combo.copy())
            if comboSum >= target or i >= len(nums):
                return

            for j in range(i, len(nums)):
                if comboSum + nums[j] > target:
                    continue
                combo.append(nums[j])
                backtrack(j, combo, comboSum + nums[j])
                combo.pop()
        
        backtrack(0, [], 0)
        return allCombos
