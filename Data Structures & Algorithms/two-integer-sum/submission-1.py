class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # SOLUTION: 
        # Maintain a map of seen nums to indexes. 
        # As you iterate through nums, if the num needed to sum to target is in the map, return that and current index
 
        seen = dict()
        for i, num in enumerate(nums):
            # If the compliment is in the set, then return this idx and seen idx
            numNeeded = target - num
            if numNeeded in seen:
                return [seen[numNeeded], i]
 
            seen[num] = i