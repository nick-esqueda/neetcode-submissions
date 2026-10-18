class Solution:
    def findMin(self, nums: List[int]) -> int:
        # The smallest num where the mid is less than the right
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + (r - l) // 2

            if nums[mid] <= nums[r]:
                r = mid
            else:
                l = mid + 1
        return nums[l]
