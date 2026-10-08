class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        need to know the product of all to left and right of curr

        [1, 2, 4, 6]
         i
        [1, 1, 2, 8]
        [48 24 6  1]
        """

        leftProducts, rightProducts = [1] * len(nums), [1] * len(nums)

        for i in range(1, len(nums)):
            leftProducts[i] = nums[i - 1] * leftProducts[i - 1]
        for i in range(len(nums) - 2, -1, -1):
            rightProducts[i] = nums[i + 1] * rightProducts[i + 1]
        
        result = [1] * len(nums)
        for i in range(len(nums)):
            result[i] = leftProducts[i] * rightProducts[i]
 
        return result
