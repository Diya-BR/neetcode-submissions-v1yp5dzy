class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxdiff = 0
        for i in range(0,len(prices)-1):
            for j in range(i+1,len(prices)):
                diff = prices[j]-prices[i]
                if diff > maxdiff:
                    maxdiff = diff
        return maxdiff

