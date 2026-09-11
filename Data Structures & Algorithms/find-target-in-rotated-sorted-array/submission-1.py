class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        [3, 4, 5, 6, 1, 2]
         l     m        r
                  lr m  

        [6, 1, 2, 3, 4, 5]
         l     m        r
         lm r       
        
        [3, 4, 5, 6, 1, 2]
         l     m        r
                  lr  m  

        1. Find the pivot point
        2. Find the num index

        pivot index is the last num in the sorted array
        """

        def findPivot(nums):
            l = 0 
            r = len(nums) - 1
            while l < r:
                mid = (l + r) // 2

                if nums[l] < nums[mid]:
                    l = mid
                else:
                    r = mid

            return l
        
        def binarySearch(nums, target, l, r):
            while l <= r:
                mid = (l + r) // 2

                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return -1

        pivot = len(nums) - 1
        if nums[0] > nums[len(nums) - 1]:
            pivot = findPivot(nums)
        
        # How do you know which side of pivot you need to search?
        l = 0
        r = len(nums) - 1
        if nums[l] <= target <= nums[pivot]:
            r = pivot
        else:
            l = pivot + 1
        
        return binarySearch(nums, target, l, r)
