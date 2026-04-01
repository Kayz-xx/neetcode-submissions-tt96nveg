class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        res = [0] * n
        stack = [] 

        for i, temp in enumerate(temperatures):
            # While the stack isn't empty AND today is hotter than the 'waiting' day
            while stack and temp > temperatures[stack[-1]]:
                prev_index = stack.pop()
                # The distance is the difference in indices
                res[prev_index] = i - prev_index
            
            # If today isn't hotter, we just add our index to the 'waiting room'
            stack.append(i)

        return res