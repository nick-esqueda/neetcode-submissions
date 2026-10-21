class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        nums: {4,10} # 4 dupe!
        used: {2, 3, 4, 5, 20}
        [2,20,4,10,3,4,5]
            i 

        "is +1 in nums?"
        "if yes, go there, and repeat"

        problem: you're wanting to add +1 count to a previous run to extend it
        but, your previous run would've recorded the full length already!

        don't start a run if num-1 is in nums!
        beacuse you KNOW you're going to find the bottom/start of the run - iter.ng over all nums!
        """

        numSet = set(nums)
        longest = 0
        for num in numSet:
            if num - 1 not in numSet: # This is the start of a run
                count = 0
                while num in numSet:
                    count += 1
                    num += 1
                longest = max(longest, count)

        return longest
