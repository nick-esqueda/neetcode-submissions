class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
        huh?????
        """
        nums.sort()
        allSubsets = []
        def backtrack(start, subset):
            # if start >= len(nums):
            allSubsets.append(subset.copy())
                # return

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                subset.append(nums[i])
                backtrack(i + 1, subset)
                subset.pop()
        
        backtrack(0, [])
        return allSubsets