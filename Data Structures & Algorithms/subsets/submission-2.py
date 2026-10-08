class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        '''
        we have an array of numbers and we need to return all 
        possibe subsets of the list. so at each stage we can 
        either pick the number or skip it.

        simple backtracking approach, define a res array, and a current
        array to go down each path of the tree. append when the index i 
        is equal to the len(nums)
        '''
        res = []
        current = []
        def backtrack(i):
            if len(nums) == i:
                res.append(current[:])
                return
            
            backtrack(i + 1)

            # pick
            current.append(nums[i])
            backtrack(i + 1)
            current.pop()

        backtrack(0)
        return res

