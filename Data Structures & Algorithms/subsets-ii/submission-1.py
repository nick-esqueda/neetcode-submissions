class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
        Take/Skip

        """
        nums.sort()
        allSubsets = []
        def backtrack(i, subset):
            if i >= len(nums):
                allSubsets.append(subset.copy())
                return
            
            # Take 
            subset.append(nums[i])
            backtrack(i + 1, subset)

            # Skip
            subset.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1, subset)

        backtrack(0, [])
        return allSubsets
