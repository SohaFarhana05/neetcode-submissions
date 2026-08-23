class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0 
        mini = prices[0]
        mindex = 0
        for i in range(1,len(prices)):
            if prices[i]<mini:
                mini = prices[i]
                mindex = i 
            if i>mindex and prices[i]>mini:
                ans = max(ans,prices[i]-mini)



        return ans 