class Solution:
    def partition(self, s: str) -> List[List[str]]:
        '''
        we have a string s, and we want to return all
        possible substrings that are palindromes. order 
        and case doesn't matter.

        the trivial way to approach this, would be very slow.
        you build all the different substrings (like subsets)
        and then find valid palindromes by using a function.
        however there should be a way where we prune the tree
        by making our decision. so we'd explore that path, use
        a base case and return. then backtrack to go back the
        parent. the challenge i have is do i keep two pointers
        at the start and end to actually check palindromes?

        at every step we either partition the string if its palindrome
        or skip partioning
        s = "aab"
        [["a","a","b"],["aa","b"]]
        at every character, we either make a decision to partition
        or skip and check a longer string down the tree. eg. aa
        '''
        def palindrome(s):
            return s == s[::-1]

        res = []
        current = []
        def backtrack(i):
            if i == len(s):
                res.append(current[:])
                return

            for j in range(i, len(s)):
                substring = s[i:j+1]
                if palindrome(substring):
                    current.append(substring)
                    backtrack(j + 1)
                    current.pop()

        backtrack(0)
        return res
        
