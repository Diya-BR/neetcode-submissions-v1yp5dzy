class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        l = 0
        r = len(heights)-1
        while l<r:
            Area = (min(heights[l],heights[r])) * (r-l)
            if maxArea < Area:
                maxArea = Area
            if heights[l] < heights[r]:
                l = l + 1
            else:
                r = r - 1
        return maxArea

