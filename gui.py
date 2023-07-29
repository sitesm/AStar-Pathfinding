import tkinter as tk
from AStar import * 
from shared import *

class AStarGUI():
    
    def __init__(self, width=600, height=500):
        # Parameters/Variables
        self.width  = 600
        self.height = 500
        self.matrix = Matrix()
        self.window = tk.Tk()
        
        # Entrys
        self.xSizeEntry = tk.Entry(self.window)
        self.ySizeEntry = tk.Entry(self.window)
        
        # Labels
        self.sizeLabel = tk.Label(self.window, text="Maze Size: ")
        self.xSeperator = tk.Label(self.window, text="x")
        
        # Window Setup
        self.window.title("AStar Algorithm Visualizer")
        self.window.geometry("{}x{}".format(self.width,self.height))

    # Removes the placeholders for the maze size inputs
    def removePlaceholder(self, event):
        widget = event.widget
        if widget == self.xSizeEntry and self.xSizeEntry.get() == 5:
            self.xSizeEntry.delete(0, tk.END)
        if widget == self.ySizeEntry and self.ySizeEntry.get() == 5:
            self.ySizeEntry.delete(0, tk.END)

    # Adds the placeholder back is no user input has been added
    def setPlaceholder(self, event):
        widget = event.widget
        if widget == self.xSizeEntry and self.xSizeEntry.get() == "":
            self.xSizeEntry.insert(0, 5)
        if widget == self.ySizeEntry and self.ySizeEntry.get() == "":
            self.ySizeEntry.insert(0, 5)

    # Validates the user only input numbers or an empty string
    def validateInput(userInput):
        return userInput.isdigit() or userInput == ""

    # Updates the maze size
    def updateMazeSize(self, event):
        # Get new size and udpate matrix accordingly
        rows = int(self.xSizeEntry.get() if (self.xSizeEntry.get() != 0 and self.xSizeEntry.get()!="") else 1)
        cols = int(self.ySizeEntry.get() if (self.ySizeEntry.get() != 0 and self.ySizeEntry.get()!="") else 1)
        self.matrix.updateSize(rows,cols)
        
        if doLogging: 
            logmsg("New # Rows: " + str(rows))
            logmsg("New # Cols: " + str(cols))
            self.matrix.printMatrix()
        
        # Create the buttons for each node in the matrix
        #for row in range(self.matrix.rows):
        #    for col in range(self.matrix.cols):
        #        node = self.matrix.getNode(row,col)
        #        node.tkButton = tk.Button(self.window, )
                

    # Creates the GUI
    def start(self):
        
        # Size selector
        self.sizeLabel.grid(row=0, column=0)
        
        # Entry boxes for user input
        self.xSizeEntry.grid(row=0, column=1)
        self.xSizeEntry.insert(0, 5)
        self.xSizeEntry.bind("<FocusIn>", self.removePlaceholder)
        self.xSizeEntry.bind("<FocusOut>", self.setPlaceholder)
        self.xSizeEntry.bind("<KeyRelease>", self.updateMazeSize)

        self.xSeperator.grid(row=0, column=2)
        
        self.ySizeEntry.grid(row=0, column=3)
        self.ySizeEntry.insert(0, 5)
        self.ySizeEntry.bind("<FocusIn>", self.removePlaceholder)
        self.ySizeEntry.bind("<FocusOut>", self.setPlaceholder)
        self.ySizeEntry.bind("<KeyRelease>", self.updateMazeSize)

        # Initalize Matrix
        self.updateMazeSize("NULL")
        
        self.window.mainloop()