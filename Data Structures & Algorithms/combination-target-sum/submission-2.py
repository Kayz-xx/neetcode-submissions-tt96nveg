class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        '''
        we are given distinct integers and we want to find 
        all the combinations that add up to target, we can
        pick one number multiple times. so at every stage we 
        reset. we can do this through a loop
        '''
        res = []
        current = []

        def backtrack(i, curr):
            if i >= len(nums) or curr < 0:
                return
            if curr == 0:
                res.append(current[:])
                return
            
            # skip
            backtrack(i + 1, curr)
            # pick
            current.append(nums[i])
            backtrack(i, curr - nums[i])
            current.pop()
        
        backtrack(0, target)
        return res
