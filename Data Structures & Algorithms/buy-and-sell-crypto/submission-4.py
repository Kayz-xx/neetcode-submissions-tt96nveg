class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        we want to find a place where we 
        return maximum profit buy buying 
        at lowest and selling at highest
        within the range of days, however
        the higher price has to occur in 
        the future and not the past

        this is a famous sliding window problem
        but there are also other ways to solve it
        i start my window at 0, 1. if my right value
        is greater than left i would reset left to 
        be right and increment right. because there 
        is no use selling at a loss. else i calculate
        profit and keep moving right. finding the max
        profit found using the max function
        '''
        left, right = 0, 1
        profit = 0
        for right in range(len(prices)):
            if prices[right] <= prices[left]:
                left = right
                right += 1
            else:
                profit = max(profit, prices[right] - prices[left])

        return profit 