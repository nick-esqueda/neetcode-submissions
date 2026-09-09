class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        SOLUTION:
        Build two lists:
        - One that holds the product of all nums to the left of that index * iteself
        - One that holds the product of all nums to the right of that index * itself
        Then, build a result list that at each index has the products to the left and right of itself, using the two lists
        
        [ 1, 2, 4, 6, 2, 3 ]
                      i                

        leftProducts  = [   1,   2,   8, 48, 96, 288 ]
        rightProducts = [ 288, 288, 144, 36,  6,   3 ]
        """

        leftProducts = [nums[0]] * len(nums)
        rightProducts = [nums[len(nums) - 1]] * len(nums)

        # Calculate & save the left products
        for i in range(1, len(nums)):
            prevProduct = leftProducts[i - 1]
            leftProducts[i] = prevProduct * nums[i]

        # Calculate & save the right products (looping & filling backwards)
        for i in range(len(nums) - 2, -1, -1):
            prevProduct = rightProducts[i + 1]
            rightProducts[i] = prevProduct * nums[i]


        # Build the result list:
        # Each index should be the product of the left and right products next to that index
        result = [rightProducts[1]] * len(nums)
        result[-1] = leftProducts[-2]
        for i in range(1, len(nums) - 1):
            leftProduct = leftProducts[i - 1]
            rightProduct = rightProducts[i + 1]
            result[i] = leftProduct * rightProduct

        return result