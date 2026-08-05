class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[-1]*(2) for _ in range(n)]
        def f(ind,buy):
            if ind==n:
                return 0
            if dp[ind][buy]!=-1:
                return dp[ind][buy]
            if buy:
                profit =  max(-prices[ind] + f(ind+1,0) , 0 + f(ind+1,1))
            else:
                profit = max(prices[ind] + f(ind+1,1) , 0 + f(ind+1,0))
            dp[ind][buy] = profit
            return dp[ind][buy] 
        return f(0,1)