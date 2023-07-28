from test import * 
from AStar import *

doTest = False
doLogging = False

def main():
    
    matrix = Matrix(3,3)
    matrix.setValue(0,1,1)
    matrix.setValue(2,1,1)
    matrix.printMatrix()
    
    # Runs tests
    if doTest:
        testInit(5)
        
    # Run algorithm
    AStar(matrix, [0,0], [2,2])
    
        
if __name__ == "__main__":
    main()