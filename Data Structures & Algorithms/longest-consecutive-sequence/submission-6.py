class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # how to track a run?
        # reset counter to 1 if the prev num isn't n-1

        if len(nums) < 2:
            return len(nums)
        
        nums.sort()
        longest = 1
        count = 1
        for i in range(1, len(nums)):
            num = nums[i]
            prevNum = nums[i - 1]

            if prevNum == num:
                continue
            
            if prevNum == num - 1:
                count += 1
            else:
                count = 1
            
            longest = max(longest, count)
        
        return longest