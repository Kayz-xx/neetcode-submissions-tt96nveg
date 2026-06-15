class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        '''
        haha i learned this in high school, let's see if i can do it
        we are trying to evaluate expressions in left-right order
        we can apply the operation on the last two operands
        and then store the result within the stack
        repeat the process

        iterate through tokens and append
        we have to use a stack to keep track of the operands
        when we reach an operation
        we perform that 
        and append the result
        '''
        stack = []

        for token in tokens:
            if token not in {"+", "-", "/", "*"}:
                stack.append(int(token))
            else:
                total = 0
                second, first = stack.pop(), stack.pop()
                if token == "+":
                    stack.append(first + second)
                elif token == "-":
                    stack.append(first - second)
                elif token == "/":
                    stack.append(int(first / second))
                else:
                    stack.append(first * second)


        return stack[-1]


        