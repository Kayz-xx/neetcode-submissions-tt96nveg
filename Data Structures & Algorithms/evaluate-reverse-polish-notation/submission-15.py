class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        '''
        we are trying evaluate reverse polish notation
        if we have an integer we push that to our stack
        if its an operation we pop the last two values
        apply the operation and push to stack
        repeat until all tokens are processes
        '''
        stack = []

        for token in tokens:
            if token == "+":
                second, first = int(stack.pop()), int(stack.pop())
                stack.append(first + second)
            elif token == "-":
                second, first = int(stack.pop()), int(stack.pop())
                stack.append(first - second)
            elif token == "*":
                second, first = int(stack.pop()), int(stack.pop())
                stack.append(first * second)
            elif token == "/":
                second, first = int(stack.pop()), int(stack.pop())
                stack.append(int(first / second))
            else:
                stack.append(int(token))
            
        return stack[-1]