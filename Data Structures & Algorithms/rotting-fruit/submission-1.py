from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        smallest num of minutes that elapse until all fruit are rotten. -1 otherwise
        lone fresh fruit won't go bad
        there may be multiple rotten to begin with

        BFS level order multi source
        each new level, counter++ (for time)

        do we need to iterate first to find count of all fresh fruits? then counter-- for fruits that become rotten?

        if exit from loop but still have fresh fruit, return -1

        [
            [1,1,0], 0
            [0,1,1], 1 
            [0,1,2]  2
             0 1 2
        ] 
        numF = 6
        minutes = 0
        q = []
        curr = ()
        """
        numFreshFruit = 0
        minutes = -1
        q = deque(list())
        visited = set()
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        isOob = lambda x, y: x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0])

        for row in range(len(grid)):
            for col, item in enumerate(grid[row]):
                if item == 1:
                    numFreshFruit += 1
                elif item == 2:
                    q.append((row, col))
        
        if not numFreshFruit:
            return 0
        
        # Handle off-by-one - include the first rotten fruits for easy placement of -= operation
        numFreshFruit += len(q)
 
        while len(q):
            for _ in range(len(q)):
                r, c = q.popleft()
                numFreshFruit -= 1

                # Add adjacent fresh fruit to queue to process as rotten later
                for dx, dy in dirs:
                    newR, newC = r + dy, c + dx
                    if (not isOob(newR, newC) 
                        and (newR, newC) not in visited 
                        and grid[newR][newC] == 1):
                        q.append((newR, newC))
                        visited.add((newR, newC))
 
            minutes += 1

        return minutes if numFreshFruit == 0 else -1