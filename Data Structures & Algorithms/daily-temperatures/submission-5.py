class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        we are trying to return a list of how many days after
        we will get a hotter temperature, so if we are on nth
        day we have to give x, where x is the number of days
        to reach a warmer temperature, 0 if there is None

        so one hint here is i already know this is a stack problem
        but apart from that let's look at this
        this would be O(n^2) as a naive solution as we check every
        element, and the ones after that
        how can i make good use of a stack here?
        '''
        n = len(temperatures)
        res = [0] * n
        for i in range(n):
            for j in range(i + 1, n):
                if temperatures[j] > temperatures[i]:
                    res[i] = (j - i)
                    break
        
        return res

