class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        count = 0

        def dfs(r, c):
            # YOUR CODE HERE
            # Think: what are your base cases?
            if r >= rows or r < 0 or c >= cols or c < 0:
                return
            if grid[r][c] == '0':
                return
            # What do you do to the current cell?
            grid[r][c] = '0'
            # What 4 directions do you recurse into?
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
            

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    count += 1
                    dfs(r, c)

        return count