class MinStack:
    '''
    okay so what we are doing here is implementing a stack
    that returns the minimum number from the stack so we have to keep
    track of that minimum variable, no effect on top and getmin
    while pushing, if the new number < min then update the min
    while popping, if we are popping the min, update to the next lowest
    we would probably need to store another list to handle this case
    this would be a sorted list storing the integers
    okay what im doing right now isn't constant time
    '''

    def __init__(self):
        self.stack = []
        self.minimum = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minimum:
            self.minimum.append(val)
        else:
            new_min = min(val, self.minimum[-1])
            self.minimum.append(new_min)
        
    def pop(self) -> None:
        self.minimum.pop()
        return self.stack.pop()
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimum[-1]
