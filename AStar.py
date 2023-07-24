from matrix import *

class Node():
    
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.f = None
        self.g = None
        self.h = None
        