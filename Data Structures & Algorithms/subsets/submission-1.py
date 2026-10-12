class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        [1, 2, 3]
 
        [1, 2, 3]
        [1, 2]
        [1, 3]
        [1]
        """
        res = []

        def backtrack(i, subset):
            if i >= len(nums):
                res.append(subset.copy()) 
                return

            # Take
            subset.append(nums[i])
            backtrack(i + 1, subset)

            # Skip
            subset.pop()
            backtrack(i + 1, subset)
        
        backtrack(0, [])
        return res