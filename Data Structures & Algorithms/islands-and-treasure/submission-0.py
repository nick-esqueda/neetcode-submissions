from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        """
        [
            [2147483647,         -1,          0, 2147483647],
            [2147483647, 2147483647, 2147483647,         -1],
            [2147483647,         -1, 2147483647,         -1],
            [         0,         -1, 2147483647, 2147483647]
        ]
        
        1. find each treasure coords
        2. starting at each coord simultaneously, BFS out (level-order) to mark each land spot
            - enqueue both treasure coords
            - for length of queue...
              - note the level (saved/updated earlier?)
              - popleft
              - set the value of this coord to the level
              - enqueue all valid neighbors

        can't do one at a time, because then you'd overwrite the old one, so have to traverse starting from all simultaneously and don't touch ones that are already set

        intuition: have to radiate outwards 1 layer/level at a time, so BFSs
        """

        visited = set()
        q = deque()
 
        for i, row in enumerate(grid):
            for j, col in enumerate(row):
                if col == 0:
                    q.append((i, j))
                    visited.add((i, j))
        
        def enqueue(grid, x, y):
            isOob = lambda x, y: (
                x < 0 or x >= len(grid) 
                or y < 0 or y >= len(grid[x]))
            if (isOob(x, y) or grid[x][y] == -1 or (x, y) in visited):
                return
            visited.add((x, y))
            q.append((x, y))
        
        level = 0
        while len(q) > 0:
            qLength = len(q)
            for _ in range(qLength):
                x, y = q.popleft()
                grid[x][y] = level

                dirs = [(0, 1),(0, -1),(1, 0),(-1, 0)]
                for dx, dy in dirs:
                    enqueue(grid, x + dx, y + dy)
 
            level += 1
                
