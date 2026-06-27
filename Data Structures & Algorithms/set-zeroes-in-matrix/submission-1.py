class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    for k in range(0, i):
                        if matrix[k][j] == 0:
                            continue
                        matrix[k][j] = float('inf')
                    for k in range (i + 1, len(matrix)):
                        if matrix[k][j] == 0:
                            continue
                        matrix[k][j] = float('inf')
                    for k in range(0, j):
                        if matrix[i][k] == 0:
                            continue
                        matrix[i][k] = float('inf')
                    for k in range(j + 1, len(matrix[0])):
                        if matrix[i][k] == 0:
                            continue
                        matrix[i][k] = float('inf')
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == float('inf'):
                    matrix[i][j] = 0

        