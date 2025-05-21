class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        mark_row = set()
        mark_column = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    mark_column.add(j)
                    mark_row.add(i)

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in mark_row or j in mark_column:
                    matrix[i][j] = 0
    
        
            
