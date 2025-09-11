class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        # count row and col seperately
        def check_palindromic(arr):
            count = 0
            left, right = 0, len(arr)-1

            while left < right:
                if arr[left] != arr[right]:
                    count += 1
                left += 1
                right -= 1

            return count
        
        row_count = 0
        for row in grid:
            row_count += check_palindromic(row)

        new_grid = [list(col) for col in zip(*grid)]
        
        col_count = 0
        for col in new_grid:
            col_count += check_palindromic(col)
        
        return min(row_count, col_count)
        

