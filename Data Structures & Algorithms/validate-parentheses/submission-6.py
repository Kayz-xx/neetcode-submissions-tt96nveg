class Solution:
    def isValid(self, s: str) -> bool:
        valid = {"}": "{", "]": "[", ")":"("}
        stack = []

        for char in s:
            if char not in valid:
                stack.append(char)
            else:
                if not stack or stack.pop() != valid[char]:
                    return False

        return len(stack) == 0