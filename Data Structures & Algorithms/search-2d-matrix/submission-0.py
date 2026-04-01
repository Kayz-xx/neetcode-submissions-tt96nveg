class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # we can obviously use binary search here
        # i'm just thinking how we seperate the rows and columns
        # do i just combine them and run binary search?
        # but that's not optimal, for sure
        
        for rows in matrix:
            l, r = rows[0], rows[-1]
            if target > r:
                continue
            left, right = 0, len(rows) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if rows[mid] < target:
                    left = mid + 1
                elif rows[mid] > target:
                    right = mid - 1
                else:
                    return True

        return False
        