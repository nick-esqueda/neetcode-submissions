class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(grid, r, c, visited):
            # Exit early if 
            # - the coord is OOB 
            # - the coord is water
            # - we've already visited this coord
            if (r < 0 or r >= len(grid)
                or c < 0 or c >= len(grid[r])
                or grid[r][c] == "0"
                or (r, c) in visited):
                return

            visited.add((r, c))
            dfs(grid, r + 1, c, visited)
            dfs(grid, r - 1, c, visited)
            dfs(grid, r, c + 1, visited)
            dfs(grid, r, c - 1, visited)
       
        visited = set() # { (0,0), (0,1) }
        count = 0
        for i, row in enumerate(grid):
            for j, num in enumerate(grid[i]):
                if num == "1" and (i, j) not in visited:
                    dfs(grid, i, j, visited)
                    count += 1
 
        return count

