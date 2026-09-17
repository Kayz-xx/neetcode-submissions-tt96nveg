class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        '''
        '''
        res = []
        current = []
        def backtrack(op, close):
            if op == n and close == n:
                res.append(''.join(current))
                return
            # open
            if op < n:
                current.append("(")
                backtrack(op + 1, close)
                current.pop()
            
            if close < op:
                current.append(")")
                backtrack(op, close + 1)
                current.pop()


        backtrack(0, 0)
        return res