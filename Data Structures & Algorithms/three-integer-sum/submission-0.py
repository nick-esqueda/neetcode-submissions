class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        target is 0

        thoughts:
        get compliment of curr num - enumerate all combos of 2 nums to make compliment?
            - no, not feasible, num can be very big
        make set of all nums - nested for loop for i & j to pin down two. if compliment in set, triplet?
            - but what about reusing same indices? keep track of index of each num? (8,1)
            - and no duplicate triplets
        sort list so we know where smaller & bigger nums would be, then two pointer?

        pin down 1 num (i), then two pointer through rest, looking for sum 0
        - [*] no use same idxs
        - [ ] no duplicate triplets
        is it possible to find a duplicate triplet with this method?

        [-1,0,1,2,-1,-4]

             *  *     *
        [-4,-1,-1,0,1,2]
             i
                  j 
                    k
        [-4,-1,-1,-1,0,1,2,2]
             i  
                   j
                         k
        once find triplet, continue next loop, otherwise might add duplicate triplet
            - NO, will miss other triplets
            - just dedupe?
            - ah, use set to maintain triplets with tuplets. convert to list of lists after
                - oh but tuplet order matters....
                - is it even possible though to have same tuplets diff order if sorted?
        also, skip any duplicates of i
        """

        nums.sort()

        triplets = set()
        for i in range(len(nums) - 2):
            if i != 0 and nums[i] == nums[i - 1]:
                continue

            l = i + 1
            r = len(nums) - 1
            while l < r:
                currSum = nums[i] + nums[l] + nums[r]
                if currSum < 0:
                    l += 1 
                elif currSum > 0:
                    r -= 1
                else:
                    triplets.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1

        return list(triplets)
        
