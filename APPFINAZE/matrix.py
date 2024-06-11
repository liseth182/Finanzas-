# matrix.py

class Matrix:
    def __init__(self, rows=1, cols=1):
        self.rows = rows
        self.cols = cols
        self.matrix = [[0 for _ in range(cols)] for _ in range(rows)]

    def add_row(self):
        self.matrix.append([0 for _ in range(self.cols)])
        self.rows += 1

    def add_column(self):
        for row in self.matrix:
            row.append(0)
        self.cols += 1

    def get_matrix(self):
        return self.matrix
