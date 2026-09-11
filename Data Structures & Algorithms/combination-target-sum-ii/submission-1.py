class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        current = []

        def backtrack(i, curr):
            if curr == 0:
                res.append(current[:])
                return
            if curr < 0 or i == len(candidates):
                return
            
            # pick
            current.append(candidates[i])
            backtrack(i + 1, curr - candidates[i])
            # backtrack
            current.pop()

            next_i = i + 1
            while next_i < len(candidates) and candidates[next_i] == candidates[i]:
                next_i += 1
            backtrack(next_i, curr)
            
        backtrack(0, target)
        return res