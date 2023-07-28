from matrix import *
from random import randint

def logmsg(message):
    print(message)
    
# Tests printing the matrix
def testInit(iters, maxRows=5, maxCols=5):
    
    # Try edgecases
    print("Default Matrix: ")
    matrix = Matrix()
    matrix.printMatrix()
    print("")
    
    print("Invalid rows: ", end='')
    try:
        matrix = Matrix(-1,5)
    except ValueError:
        print("Success")
    print("")
    
    print("Invalid cols: ", end='')
    try:
        matrix = Matrix(5,-1)
    except ValueError:
        print("Success")
    print("")
    
    for i in range(iters):
        rows = randint(1,maxRows)
        cols = randint(1,maxCols)
        
        print("{}x{}: ".format(rows,cols))
        matrix = Matrix(rows,cols)
        matrix.printMatrix()
        print("")
