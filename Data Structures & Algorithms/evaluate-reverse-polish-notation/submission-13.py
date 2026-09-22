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
            if token not in {"+", "-", "/", "*"}:
                stack.append(int(token))
            else:
                second, first = stack.pop(), stack.pop()
                if token == "+":
                    stack.append(first + second)
                elif token == "-":
                    stack.append(first - second)
                elif token == "*":
                    stack.append(first * second)
                else:
                    stack.append(int(first / second))
            
        return stack[-1]