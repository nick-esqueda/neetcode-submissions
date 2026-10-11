class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        Unique quadruplets (order unique)
        Must be distinct - can't use same number twice
        All sum to target

        With a certain 'a', and a certain 'b', and a certain 'c', what 'd' gets me target?

        Store compliment in set with idx
        If come across compliment, obv 

        [3,2,3,-3,1,0]
         a 
           b
             c
                d

        [-3,0,1,2,3,3]               
          a 
               b
                 c
                     d
        
        Does knowing where pos vs neg numbers help?

        "Everything after idx is 

        3sum:
        - Sort arr
        - A is pinned, so,
        - Do two pointer with rest of arr to find sum

        Does it make sense to....
        Hit target with only 3 nums, then,
        Find 0 with 4th
        NO


        - Sort arr
        - A is pinned, so,
        - Do two pointer with rest of arr to find sum
        - Also, before, collect inside nums in two pointer space in set
        - Each two pointer iter, check if compliment is in set
        - If so, return all those.
        - Keep going?

        [-3, 0, 3, 3]
        t = 3
        [-3,0,1,2,3,3]               
          a 
            b
                    c
        d = {1, 2, 3}
        """
        result = []
        nums.sort()

        for a in range(len(nums) - 3):
            if a > 0 and nums[a] == nums[a - 1]:
                continue
            for b in range(a + 1, len(nums) - 2):
                if b > a + 1 and nums[b] == nums[b - 1]:
                    continue

                twoSum = nums[a] + nums[b]
 
                c, d = b + 1, len(nums) - 1
                while c < d:
                    currSum = twoSum + nums[c] + nums[d]
                    if currSum < target:
                        c += 1
                    elif currSum > target:
                        d -= 1
                    else:
                        result.append([nums[a], nums[b], nums[c], nums[d]])

                        # Skip duplicates of C and D
                        while c < d and nums[c] == nums[c + 1]:
                            c += 1
                        while c < d and nums[d] == nums[d - 1]:
                            d -= 1

                        c += 1
                        d -= 1

        return result

