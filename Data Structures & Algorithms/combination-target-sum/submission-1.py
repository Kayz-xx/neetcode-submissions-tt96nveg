class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        '''
        we are trying to find all possible combinations 
        from a list to add to a target number. 
        we need to approach this by using backtracking, again
        imagine that this problem can be solved by either picking
        or not picking a number, where one can be repeated.
        this is a bit similar to twosum, but there are again different ways 
        to do this. we either backtrack by decrementing the target each time
        to see the current valur required. so we pick a value, decrement the target
        call function recursively with the updated values until we reach a target of 0, then
        backtrack by resetting the target to the default value.

        '''
        res = []
        current = []

        def backtrack(i, curr):
            if curr == 0:
                res.append(current[:])
                return
            if curr < 0 or i == len(nums):
                return
            
            # skip
            backtrack(i + 1, curr)
            current.append(nums[i])
            backtrack(i, curr - nums[i])
            current.pop()
        
        backtrack(0, target)
        return res
