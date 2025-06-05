class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        row_length = len(maze)
        col_length = len(maze[0])
        queue = deque([(entrance[0], entrance[1], 0)])
        visited = set() # (row, column)
        visited.add((entrance[0], entrance[1]))
        res = float('inf')

        while queue:
            cur_row, cur_col, count = queue.popleft()
            if cur_row == 0 or cur_row == row_length-1 or cur_col == 0 or cur_col == col_length-1:
                if [cur_row, cur_col] != entrance:
                    res = min(res, count)
                    
            if (cur_row-1, cur_col) not in visited and cur_row-1 >= 0 and maze[cur_row-1][cur_col] == ".":
                visited.add((cur_row-1, cur_col))
                queue.append((cur_row-1, cur_col, count+1))
            if (cur_row, cur_col-1) not in visited and cur_col-1 >= 0 and maze[cur_row][cur_col-1] == ".":
                visited.add((cur_row, cur_col-1))
                queue.append((cur_row, cur_col-1, count+1))
            if (cur_row+1, cur_col) not in visited and cur_row+1 < row_length and maze[cur_row+1][cur_col] == ".":
                visited.add((cur_row+1, cur_col))
                queue.append((cur_row+1, cur_col, count+1))
            if (cur_row, cur_col+1) not in visited and cur_col+1 < col_length and maze[cur_row][cur_col+1] == ".":
                visited.add((cur_row, cur_col+1))
                queue.append((cur_row, cur_col+1, count+1))
        
        return res if res != float('inf') else -1
                


