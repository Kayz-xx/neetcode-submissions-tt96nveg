class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # we are not using this boomer ass approach get to DP 
        # profit = 0
        # left = 0
        # right = 1
        # while right < len(prices):
        #     if prices[right] < prices[left]:
        #         left = right
        #     else:
        #         profit = max(profit, prices[right] - prices[left])
        #     right += 1
        # return profit
        if not prices:
            return 0
        dp = [0] * len(prices)
        min_buy = prices[0]
        for i in range(1, len(prices)):
            min_buy = min(min_buy, prices[i])
            dp[i] = max(dp[i - 1], prices[i] - min_buy)
        
        return dp[-1]