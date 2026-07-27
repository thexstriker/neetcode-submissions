class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lInd = len(prices)-2
        rInd = len(prices)-1
        maxDiff = prices[rInd] - prices[lInd]

        while(lInd >= 0):
            if(prices[lInd] > prices[rInd]):
                rInd = lInd
                lInd = rInd - 1
            while(lInd >= 0 and prices[lInd] <= prices[rInd]):
                maxDiff = max(maxDiff, prices[rInd] - prices[lInd])
                lInd -= 1
        
        if(maxDiff <= 0):
            return 0
        return maxDiff