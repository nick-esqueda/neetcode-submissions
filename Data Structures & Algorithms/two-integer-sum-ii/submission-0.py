class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        has to return 1-indexed result 
        result = [idx1, idx2] -> the indexes of nums that equal to target
        cannot use the same number twice - can't return both of same index
        """

        l = 0
        r = len(numbers) - 1

        while l < r:
            currSum = numbers[l] + numbers[r]

            if currSum < target:
                l += 1
            elif currSum > target:
                r -= 1
            else:
                return [l + 1, r + 1]
