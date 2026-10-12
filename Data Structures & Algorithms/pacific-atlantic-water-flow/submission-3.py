class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        """
        rows, cols = len(heights), len(heights[0])
        pacCells, atlCells = set(), set()
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        isOob = lambda x, y: (
            x < 0 or y < 0 or x >= len(heights) or y >= len(heights[0])
        )

        def dfs(r, c, cellSet):
            if isOob(r, c) or (r, c) in cellSet:
                return
            
            cellSet.add((r, c))

            for dx, dy in dirs:
                newR, newC = r + dx, c + dy
                if (not isOob(newR, newC) 
                    and heights[newR][newC] >= heights[r][c]):
                    dfs(newR, newC, cellSet)

        # Pacific cells
        for c in range(cols):
            dfs(0, c, pacCells)
        for r in range(rows):
            dfs(r, 0, pacCells)

        # Atlantic cells
        for c in range(cols):
            dfs(rows - 1, c, atlCells)
        for r in range(rows):
            dfs(r, cols - 1, atlCells)
        
        return list(pacCells & atlCells)