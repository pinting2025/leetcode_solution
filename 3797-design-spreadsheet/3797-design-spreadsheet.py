class Spreadsheet:
    def __init__(self, rows: int):
        self.grid = {}
        start_char = 'A'
        
        for i in range(26):
            col = chr(ord(start_char)+i)
            self.grid[col] = [0] * rows

    def setCell(self, cell: str, value: int) -> None:
        cell = list(cell)
        col = cell[0]
        row = int("".join(cell[1:]))
        self.grid[col][row-1] = value
        return

    def resetCell(self, cell: str) -> None:
        cell = list(cell)
        col = cell[0]
        row = int("".join(cell[1:]))
        self.grid[col][row-1] = 0
        return 

    def getValue(self, formula: str) -> int:
        formula = list(formula)
        cur = 1
        x = list()
        
        while formula[cur] != "+":
            x.append(formula[cur])
            cur += 1

        y = formula[cur+1:]

        def get_cell_value(cell):
            if cell[0] in self.grid:
                row = int("".join(cell[1:]))
                return self.grid[cell[0]][row-1]
            else:
                return int("".join(cell))
        
        x = get_cell_value(x)
        y = get_cell_value(y)
        
        return x+y
        


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)