class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        need a window to hit (or exceed) target
        - if none return 0
        want the smallest window
        need to check all windows anyways
        not sorted, and can't because window needs to be original order

        sliding window 
        track window size via counter?
        when to expand/shrink window?
        maybe just when you've exceeded target
        - obv, if we're over target, expanding makes no sense. start shrinking window until under target again to keep searching
        if R hits end, done

        target = 10
        min = 3       # smallest window - can only update when sum >= target
        sum = 3       # running sum
        [2, 1, 5, 1, 5, 3]
         i
               j 
        """


        minLen = float('inf')
        windowSum = 0
        i, j = 0, 0
        while j < len(nums):
            windowSum += nums[j]

            while windowSum >= target:
                minLen = min(minLen, j - i + 1)
                windowSum -= nums[i]
                i += 1

            j += 1

        return minLen if minLen != float('inf') else 0
