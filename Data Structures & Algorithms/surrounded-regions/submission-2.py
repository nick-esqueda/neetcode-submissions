class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        There are "unsurrounded" regions - groups of Os that touch the edge
        If a region is connected to an O touching the edge, then it is NOT surrounded.

        Need to detect where unsurrounded regions are and fix them

        - Iterate from all edges first and save all cells of unsurrounded regions in set
        - Iterate through board, ignore unsurrounded regions
        - When you see a O that's NOT in the set, mark all of those as X
        """

        unsurrounded = set()
        ROWS, COLS = len(board), len(board[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        isOob = lambda x, y: x < 0 or y < 0 or x >= ROWS or y >= COLS
 
        def dfs(r, c):
            if (isOob(r, c) 
                or (r, c) in unsurrounded
                or board[r][c] != "O"):
                return
            
            unsurrounded.add((r, c))
            
            for dx, dy in dirs:
                dfs(r + dx, c + dy)

        # Top, Bottom
        for c in range(COLS):
            dfs(0, c)
            dfs(ROWS - 1, c)
        
        # Left, Right
        for r in range(ROWS):
            dfs(r, 0)
            dfs(r, COLS - 1)
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and (r, c) not in unsurrounded:
                    board[r][c] = "X"


