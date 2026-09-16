class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        In other words, find the pivot point

        Using Binary Search Template, need to define the monotonic boolean condition 
        (i.e. define the condition that makes the list [ F F F T T T ] so we can find the first True)
        Condition: "mid <= nums[-1]"
        Looking for the first number that is less than the last num in list
        """

        l = 0 
        r = len(nums) - 1
        while l < r:
            mid = l + (r - l) // 2

            if nums[mid] <= nums[-1]:
                # Mid could still be the answer - include it
                r = mid
            else:
                # Mid cannot be the answer - exclude it
                l = mid + 1
        return nums[l]
 