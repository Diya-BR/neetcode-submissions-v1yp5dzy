class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        for i in range(len(heights)-1):
            for j in range(i+1, len(heights)):
                Area =(min( heights[i] , heights[j])*abs(i-j))
                
                if Area > maxArea:
                   maxArea = Area
        return maxArea 
