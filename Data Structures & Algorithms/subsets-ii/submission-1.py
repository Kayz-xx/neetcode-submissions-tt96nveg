class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        '''
        we are trying to return subsets without duplicates
        so at every stage we have pick or don't pick
        however the additional constraint is that we now 
        have duplicate integers that will create the same subset

        we approach the problem with backtracking, starting with
        an empty current array and going through the choices,
        once we reach a leaf in the tree we terminate. (i == len(nums))
        the problem here is we can't just skip to next_i like in 3 sum
        or combinationsum2, because that ignores repeated subsets like
        [1, 1] or [1, 1, 2]
        the naive way here would to be remove duplicates from the final res array
        '''
        nums.sort()
        res = []
        current = []

        def backtrack(i):
            if i == len(nums):
                res.append(current[:])
                return

            # skip
            next_i = i + 1
            while next_i < len(nums) and nums[next_i] == nums[i]:
                next_i += 1
            backtrack(next_i)
            # pick
            current.append(nums[i])
            backtrack(i + 1)
            current.pop()

        backtrack(0)
        return res