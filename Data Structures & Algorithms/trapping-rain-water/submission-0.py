class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        l_max = 0
        r_max = 0
        sum = 0
        while l<r:
            if height[l] < height[r]:
                l_max = max(height[l],l_max)
                sum += l_max - height[l]
                l += 1
            else:
                r_max = max(height[r],r_max)
                sum += r_max - height[r]
                r -= 1
        return sum

                

        