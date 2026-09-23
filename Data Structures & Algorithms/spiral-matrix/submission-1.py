class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        topRow = 0
        bottomRow = len(matrix) - 1
        leftCol = 0
        rightCol = len(matrix[0]) - 1
        result = list()
        
        while topRow <= bottomRow and leftCol <= rightCol:

            # Top/Right
            for i in range(leftCol, rightCol + 1):
                result.append(matrix[topRow][i])
            topRow += 1

            # Right/Down
            for i in range(topRow, bottomRow + 1):
                result.append(matrix[i][rightCol])
            rightCol -= 1

            # Bottom/Left
            if topRow <= bottomRow:
                for i in range(rightCol, leftCol - 1, -1):
                    result.append(matrix[bottomRow][i])
                bottomRow -= 1

            # Left/Up
            if leftCol <= rightCol:
                for i in range(bottomRow, topRow - 1, -1):
                    result.append(matrix[i][leftCol])
                leftCol += 1
        
        return result

