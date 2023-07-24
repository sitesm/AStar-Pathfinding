from matrix import *
from random import randint

# Tests printing the matrix
def testInit(iters, maxRows=20, maxCols=20):
    
    # Try edgecases
    print("Default Matrix: ")
    matrix = Matrix()
    matrix.printtMatrix()
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
        matrix.printtMatrix()
        print("")
