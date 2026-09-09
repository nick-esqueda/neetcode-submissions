class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            num = nums[i]
            prev = nums[i - 1]
            if num == prev:
                return True
        return False