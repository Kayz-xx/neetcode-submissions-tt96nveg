class Solution:
    def isValid(self, s: str) -> bool:
        # we are trying to validate brackets
        # every opening bracket requires the same closing bracket
        # we need to keep track of the last bracket
        # now how do we make use of a stack (LIFO)

        # i push all the opening brackets onto the stack
        # pop the latest element
        # we check for matches using a hash map
        # check if the current parenthesis matches, if not exit
        
        stack = []
        parenthesis_map = {"(": ")", "[": "]", "{": "}"}

        for char in s:
            if char in parenthesis_map:
                stack.append(char)
            elif stack:
                if parenthesis_map[stack.pop()] != char:
                    return False
            else:
                return False

        return len(stack) == 0