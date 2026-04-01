class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for item in tokens:
            if item in ["+", "-", "/", "*"]:
                op1, op2 = stack.pop(), stack.pop()
                if item == '+':
                    stack.append(op1 + op2)
                elif item == '-':
                    stack.append(op2 - op1)
                elif item == '/':
                    stack.append(int(op2 / op1))
                else:
                    stack.append(op1 * op2)
            else:
                stack.append(int(item))


        return stack[0]