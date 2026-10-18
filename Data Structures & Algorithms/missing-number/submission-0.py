class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        XOR to a var from 0 to n
        XOR again for each num in nums
        What's left is what's missing
        """
        base = 0
        for n in range(len(nums) + 1):
            base ^= n

        for num in nums:
            base ^= num
        
        return base
