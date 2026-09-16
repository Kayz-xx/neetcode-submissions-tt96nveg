class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        '''
        we are now trying to find every permutation instead of combination,
        so each permutation has different order but includes every element

        so now have to pick every value, but at point there are len(arr) choices
        [1/2/3, 2/3, 3]. so we can see that we can pick a number ONLY once since
        every integer is unique. we want to pick every integer and the order doesn't
        matter so we can pick any starting integer. from there we then pick values
        that we haven't chosen already
        initialize a res array
        initialize a current array for each permutation

        define a backtrack function:
            if i == len(nums): (or could be something else, but let's say we're using indices)
                res.append(current[:])

            current.append(nums[i])
            backtrack(i, arr)
            current.pop()

        call backtrack on array
        return final res
        '''

        res = []
        current = []
        used = [False] * len(nums)

        def backtrack():
            if len(current) == len(nums):
                res.append(current[:])
                return
        
            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i] = True
                current.append(nums[i])
                backtrack()
                current.pop()
                used[i] = False
            
        backtrack()
        return res