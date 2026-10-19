class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        - Find pivot with binary search optimal value
        - Find which side target is in
        - Binary search that side
        """

        # Find pivot with binary search optimal value
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + (r - l) // 2

            if nums[mid] <= nums[-1]:
                r = mid
            else:
                l = mid + 1
        
        # Find which side target is in
        if nums[l] <= target <= nums[-1]:
            r = len(nums) - 1
        else:
            r, l = l, 0

        # Search the proper side for the target
        while l <= r:
            mid = l + (r - l) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1

        return -1
        