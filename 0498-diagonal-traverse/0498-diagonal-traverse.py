class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        # use cell position sum (row+col) to keep track of the direction
        row_len = len(mat)
        col_len = len(mat[0])
        res = [mat[0][0]]
        row = 0
        col = 0

        while len(res) < row_len*col_len:
            # move up right
            if (row+col) % 2 == 0:
                # move up right
                if row - 1 >= 0 and col + 1 < col_len:
                    row -= 1
                    col += 1
                # change direction
                else:
                    if col+1 < col_len:
                        col += 1
                    elif row+1 < row_len:
                        row += 1

            else:
                # move down left
                if row + 1 < row_len and col - 1 >= 0:
                    row += 1
                    col -= 1
                # change direction
                else:
                    if row+1 < row_len:
                        row += 1
                    elif col+1 < col_len:
                        col += 1
            
            res.append(mat[row][col])
        
        return res



            
            
