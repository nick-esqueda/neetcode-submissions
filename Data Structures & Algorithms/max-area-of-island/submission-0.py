class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        def findArea(grid, r, c, visited):
            # OOB, 1 vs 0, in visited
            if (r < 0 or r >= len(grid)
                or c < 0 or c >= len(grid[r])
                or grid[r][c] == 0
                or (r, c) in visited):
                return 0
            
            visited.add((r, c))
            
            dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            totalArea = 1
            for dx, dy in dirs:
                dirArea = findArea(grid, r + dx, c + dy, visited)
                totalArea += dirArea
            
            return totalArea

        visited = set()
        maxArea = 0
        for r, row in enumerate(grid):
            for c, num in enumerate(row):
                if num == 1 and (r, c) not in visited:
                    area = findArea(grid, r, c, visited)
                    maxArea = max(maxArea, area)
        
        return maxArea