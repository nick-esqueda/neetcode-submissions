class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        need to know if the board is valid. valid constraints:
        - each row can only contain digits 1-9. can NOT have duplicates
        - each column ...
        - each 3x3 box ...

        1. check all rows, confirm valid or not
        2. check all columns, confirm valid or not
        3. check all boxes, confirm valid or not
            - how to do this?
            - just need to know what row/col you're on. divide (floor) idx by 3 to get bucket

        maintain sets for all rows/columns/boxes?
        as you iterate, check the row/col/box set if num exists. if yes, it's a dupe.
        """

        rowSets = [set() for _ in range(9)]
        colSets = [set() for _ in range(9)]
        boxSets = {
            "0,0": set(),
            "1,0": set(),
            "2,0": set(),
            "0,1": set(),
            "1,1": set(),
            "2,1": set(),
            "0,2": set(),
            "1,2": set(),
            "2,2": set(),
        }

        for rowIdx, row in enumerate(board):
            for colIdx, num in enumerate(row):
                if num == ".":
                    continue

                boxKey = f"{rowIdx // 3},{colIdx // 3}"

                if (num in rowSets[rowIdx] or 
                    num in colSets[colIdx] or
                    num in boxSets[boxKey]):
                    return False
                    
                rowSets[rowIdx].add(num)
                colSets[colIdx].add(num)
                boxSets[boxKey].add(num)
        
        return True
        










