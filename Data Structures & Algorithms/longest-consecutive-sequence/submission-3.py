class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        PROBLEM STATEMENT: 
        return the length of the longest consecutive sequence of numbers that you can make using the numbers in nums.
        the original list order doesn't matter (can find consecutive in any order)
        positive/negative consecutive doesn't really matter - same basically

        NOTES:
        while loop? hash set/map? 
        put all nums in a hash set
        loop over nums list
        if you come across this num +1 in set, then you can start investigating
        - try to iterate over set, counting up to see if +1 is in set 
        keep track of longest run

        need to avoid running along same path (run) of nums
        how to detect if we're running along a previous run?
        1. maintain ANOTHER set - visited?
            - visited set will have the nums we did a run over.
            - if num + 1 (or num?) is in visited, then....
                - could we add 1 to the maxLength? but might not be the right run...
                    - can't just blindly add 1
                - if the number was 
                - if num is in visited, then we already calculated a run with that num
                - if 
                
            - how do I know the length of a run when I see a num in visited?
            
        v = {2,3,4,5, 10,11,12}
        runSet = {2,20,4,10,3,4,5}
        nums   = [2,20,4,10,3,4,5]
                       i               

        maybe need to associate nums that were part of a run?

        {2,20,4,10,3,4,5}
                       2 
        [2,20,4,10,3,4,5]
              i
        longest = 4
        
        --- 
 
        problem: what if you can't 
        bad: "i can just add +N to the longest then!"
        store the max (or min?) num in the longest run?
        {5, 4, 3, 2, 1, 10, 9, 8}
                        r      
        [5, 4, 3, 2, 1, 10, 9, 8]
                            i         
        longest = 6
        """

        if len(nums) == 0:
            return 0
        
        numSet = set(nums)
        maxLength = 1
        for num in nums:
            # Don't start looping if this num could be the middle of a run
            # i.e., Only start looping if this could be the start of a run
            if num - 1 in numSet:
                continue

            tempNum = num
            length = 1
            while tempNum + 1 in numSet:
                tempNum += 1
                length += 1
 
            maxLength = max(maxLength, length)
        
        return maxLength
