class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        mapping = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7":"pqrs", "8": "tuv", "9": "wxyz"}
        res = []
        current = []
        def backtrack(i):
            if i == len(digits):
                res.append("".join(current))
                return
            
            seq = mapping[digits[i]]
            for char in seq:
                current.append(char)
                backtrack(i + 1)
                current.pop()

        backtrack(0)
        return res
