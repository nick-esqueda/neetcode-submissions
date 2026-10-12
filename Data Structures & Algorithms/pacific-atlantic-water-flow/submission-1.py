from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        Return all cells that can get water to flow into BOTH oceans
        High -> low cells -> ocean
 
        Shortest path vs any path?
        > BFS multi-source?
        How to determine where the ocean is?
        > If you can get to a border cell, that's it
        Can the corner cells flow water into the Pacific AND Atlantic?
        > Yes
        Will corners always be in the result?
        > Yes
        Favor certain routes to get to P or A faster?
        > ...

        
        At each cell, start multi-source BFS
        If can get to both P and A, return early and save cell
        Move on to next
        """

        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        isPacific = lambda x, y: x == 0 or y == 0
        isAtlantic = lambda x, y: x == len(heights) - 1 or y == len(heights[0]) - 1
        isOob = lambda x, y: (
            x < 0 or y < 0 or x >= len(heights) or y >= len(heights[0])
        )

        def canReachBothOceans(startR, startC):
            foundPacific = False
            foundAtlantic = False
            visited = set()
            q = deque([(startR, startC)])
            while q:
                for _ in range(len(q)):
                    r, c = q.popleft()

                    if isPacific(r, c):
                        foundPacific = True
                    if isAtlantic(r, c):
                        foundAtlantic = True

                    if foundPacific and foundAtlantic:
                        return True
                    
                    # Add neighbors to queue
                    for dx, dy in dirs:
                        newR, newC = r + dx, c + dy
                        if (not isOob(newR, newC)
                            and (newR, newC) not in visited
                            and heights[newR][newC] <= heights[r][c]):
                            visited.add((newR, newC))
                            q.append((newR, newC))
            return False
        
        result = []
        for r, row in enumerate(heights):
            for c, col in enumerate(row):
                if canReachBothOceans(r, c):
                    result.append((r, c))

        return result