class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        IN-PLACE VARIANT
        """
        
        allPerms = []
        def backtrack(start):
            if start >= len(nums):
                allPerms.append(nums.copy())
                return

            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1)
                nums[start], nums[i] = nums[i], nums[start]

        backtrack(0)
        return allPerms