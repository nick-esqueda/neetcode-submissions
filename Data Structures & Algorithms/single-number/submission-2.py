class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        XOR
        XORing a number twice onto the same base cancels them out.
        So, if all nums are doubled except one, the doubles will cancel out, leaving the one.
        """
        count = 0
        for num in nums:
            count ^= num
        return count
