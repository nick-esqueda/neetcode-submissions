class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        currSubset = []

        def getSubsets(i):
            if i >= len(nums):
                res.append(currSubset.copy())
                return

            # Decide to add number
            currSubset.append(nums[i])
            getSubsets(i + 1)
 
            # Decide to remove number
            currSubset.pop()
            getSubsets(i + 1)
 
        getSubsets(0)
        return res