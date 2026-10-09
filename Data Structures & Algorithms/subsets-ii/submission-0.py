class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
        All possible subsets
        Solution CAN'T have duplicate subsets
        - [2,1] and [1,2] are duplicate subsets
        Think like Sets. Subsets. Order doesn't matter, in a way

        Need explicitly handle subsets

        Take/Skip

        What goes in this spot? Nothing, this one, next one
        Have to keep track of remaining
        Remaining in order?

        "If you skip it, you really wanna skip it"
        "... Because you already considered all possibilities using this number (+ dupes)"
      
                                               [1,2,1]
                                               [_,_,_]
                              [1]                                 []
                  [1, 2]              [1]                  [2]           []
        [1, 2, 1]     [1, 2]    [1,1]      [1]      [2,1]            [1]      []
        """

        allSubsets = []
        nums.sort()
 
        def backtrack(i, subset):
            if i >= len(nums):
                allSubsets.append(subset.copy())
                return

            # Take
            subset.append(nums[i])
            backtrack(i + 1, subset)

            # Skip over dupe nums to avoid dupe subsets
            # Already considered all combinations using the num above with Take
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
 
            # Skip
            subset.pop()
            backtrack(i + 1, subset)
 
        backtrack(0, [])
        return allSubsets
        