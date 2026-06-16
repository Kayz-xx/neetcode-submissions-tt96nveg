class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        '''
        we have n cars travelling on a one-lane highway
        each car has a unique position and speed
        their desintation is at target miles
        a fleet is a collection of cars
        a car cannot pass another car, they become part of the same
        fleet when at the same position
        we want to return the number of fleets that reach the target

        my initial working is to use time in some way
        we know the formula of s=d/t where d = target - position
        now i have to make sense of how we can use a stack here
        okay so i found that if we are behind and have a lower arrival time
        then we join fleet.
        each position is unique so we can sort
        '''
        combined = list(zip(position, speed))
        combined.sort(reverse=True)
        stack = []  
        for position, speed in combined:
            time = (target - position) / speed
            if not stack or time > stack[-1]:
                stack.append(time)

        return len(stack)
