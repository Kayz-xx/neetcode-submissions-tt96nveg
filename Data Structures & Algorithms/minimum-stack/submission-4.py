class MinStack:
    '''
    we are trying to implement a modified stack with a constraint
    we want a new operation to return the minimum value of the stack
    all should be constant time, no sorting allowed
    so we need to handle this on push and pop

    i will implement a basic stack with standard operations
    we need another stack that is ordered (ascending)
    my main issue is how do insert in perfect order
    in constant time, without looking at all elements
    '''

    def __init__(self):
        self.stack = []
        self.min_stack = []
        self.val = float('inf')
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        self.val = min(val, self.val)
        self.min_stack.append(self.val)

    def pop(self) -> None:
        self.stack.pop()
        self.val = self.min_stack.pop()
        self.val = self.min_stack[-1] if self.min_stack else float('inf')

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
