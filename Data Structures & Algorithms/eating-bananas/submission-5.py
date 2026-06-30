class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
        what kind of a dumb problem is this,
        we're trying to return the minimum rate k
        such that we can eat all bananas with h hours,
        so it is a greedy problem

        we can first sort the array to find the largest
        pile, we chose that as our initial rate?
        then we run binary search to find the point of
        optimality, where we equal or less than h. 
        '''
        piles.sort()
        left, right = 1, piles[-1]

        rate = right
        while left <= right:
            mid = (left + right) // 2
            hours = sum(math.ceil(pile / mid) for pile in piles)
            if hours <= h:
                right = mid - 1
                rate = min(rate, mid)
            elif hours > h:
                left = mid + 1

        return rate 

