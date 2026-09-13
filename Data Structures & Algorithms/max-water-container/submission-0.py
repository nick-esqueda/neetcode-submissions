class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        """

        currMaxArea = 0
        l = 0
        r = len(heights) - 1
        while l < r:
            width = r - l
            height = min(heights[r], heights[l])
            area = width * height

            currMaxArea = max(currMaxArea, area)

            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1

        return currMaxArea