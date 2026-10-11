class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        word = "ABCESEEEFS"
        [
            ["A","B","C","E"],
            ["S","F","E","S"],
            ["A","D","E","E"]
        ] 
        """
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        isOob = lambda r, c: (
            r < 0 or c < 0 or r >= len(board) or c >= len(board[0])
        )

        def hasWord(r, c, i, visited):
            if i >= len(word):
                return True
            if (isOob(r, c) 
                or (r, c) in visited
                or board[r][c] != word[i]):
                return False

            visited.add((r, c))

            for dx, dy in dirs:
                found = hasWord(r + dx, c + dy, i + 1, visited)
                if found:
                    return True
            
            visited.remove((r, c))
            return False


        for r, row in enumerate(board):
            for c, char in enumerate(row):
                if board[r][c] == char:
                    if hasWord(r, c, 0, set()):
                        return True

        return False
