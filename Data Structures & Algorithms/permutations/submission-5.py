class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        IN-PLACE VARIANT

        Use a start index and move all used nums to before it
        Manipulating what the next frame sees/can choose

        Swapping has to happen in a loop
        Swap i+1 with i? Or need to strech further?

        [2, 1, 3]
         i

        [_, _, _]
        [1, 2, _]
        [1, 2, 3]
        [1, 3, 2]
        [3, _, _]
        [3, 1, 2]
        [3, 2, 1]
        [3, _, _]
        [2, _, _]
        [2, 3, _]
        [2, 3, 1]
        [2, 1, 3]
        [2, 1, _]
        """
        
        allPerms = []
        def backtrack(start):
            if start >= len(nums):
                allPerms.append(nums.copy())
                return

            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1)
                nums[start], nums[i] = nums[i], nums[start]

        backtrack(0)
        return allPerms