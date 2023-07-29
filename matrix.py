from shared import *

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
            newRow = []
            for col in range(self.cols):
                node = Node(row,col,0)
                newRow.append(node)
            self.matrix.append(newRow)
    
    def setValue(self, row, col, val):
        self.matrix[row][col].value = val
    
    # Clears matrix and re initalizes new size
    # Destroys all buttons in the process
    def updateSize(self, newRows, newCols):
        self.destroyButtons()
        self.rows = newRows
        self.cols = newCols
        self.matrix.clear()
        self.initMatrix()
     
    # Destorys every nodes button
    def destroyButtons(self):
        for row in range(self.rows):
            for col in range(self.cols):
                node = self.getNode(row,col)
                if node.tkButton != None:
                    node.tkButton.destroy()
                    node.tkButton = None
                       
    # Returns the node at the given row/column
    def getNode(self, row, col):
        return self.matrix[row][col]
        
    # Prints matrix
    def printMatrix(self):
        for row in self.matrix:
            print("[", end='')
            for col in row:
                print(str(col.value) + ",", end='') if col != row[-1] else print(str(col.value), end='')
            print("]")
        print("\n")

            
class Node():
    
    def __init__(self, row, col, value):
        self.row = row
        self.col = col
        self.f = float('inf')
        self.g = float('inf')
        self.h = float('inf')
        self.parent = None
        self.value = value
        self.tkButton = None
    
    # Gets the huristic estimation to the end node
    def setHuristic(self, endCords):
        # Pathageran therom estimation
        self.h = (self.row - endCords[0])**2 + (self.col-endCords[1])**2   

    def __str__(self):
        return "({},{}): f={},g={},h={}".format(self.row,self.col,self.f,self.g,self.h)
        
