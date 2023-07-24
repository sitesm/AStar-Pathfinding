
class Matrix():
    
    def __init__(self, rows=5, cols=5):
        # Error check
        if rows<=0:
            raise ValueError("Rows must be GTE 0")
        if cols<=0:
            raise ValueError("Cols must be GTE 0")
        
        # Object Variables
        self.matrix = []
        self.rows = rows
        self.cols = cols
        self.initMatrix()
        
    # Initalizes a clean matrix
    def initMatrix(self):
        for row in range(self.rows):
            row = []
            for col in range(self.cols):
                row.append(0)
            self.matrix.append(row)
    
    # Prints matrix
    def printtMatrix(self):
        for row in self.matrix:
            print(row)
