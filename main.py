from test import * 
from AStar import *
from gui import *
from shared import *

def main():
    # Runs tests
    if doTest:
        testInit(5)
    
    GUI = AStarGUI()
    GUI.start()
        
if __name__ == "__main__":
    main()