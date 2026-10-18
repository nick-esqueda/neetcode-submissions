class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        target = 0

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l = i + 1
            r = len(nums) - 1
            while l < r:
                sum_ = nums[i] + nums[l] + nums[r]
                if sum_ < target:
                    l += 1
                elif sum_ > target:
                    r -= 1
                else:
                    result.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < len(nums) and nums[l] == nums[l - 1]:
                        l += 1
                    while r > 0 and nums[r] == nums[r + 1]:
                        r -= 1
        return result
