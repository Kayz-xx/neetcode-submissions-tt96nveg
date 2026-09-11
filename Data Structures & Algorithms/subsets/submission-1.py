class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        '''
        we are trying to build all possible subsets of a list
        it means we have two choices for each item
        we either pick it or we don't pick,
        we do this recursively through backtracking
        '''
        res = []
        curr = []

        def backtrack(i):
            # when we reach the terminal point,
            # end of tree, append the result (could be empty if we didn't pick anything)
            if i == len(nums):
                res.append(curr[:])
                return
            # skip
            backtrack(i + 1)
            # include
            curr.append(nums[i])
            backtrack(i + 1)
            curr.pop()
        
        backtrack(0)
        return res