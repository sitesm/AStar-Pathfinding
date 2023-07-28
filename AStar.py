from matrix import *
from main import doLogging
from test import logmsg 

# returns a list of all neighboring nodes (with bound checking)
def getNeighbors(matrix, node, xbound, ybound):
    currRow = node.row
    currCol = node.col
    neighbors = []
    
    # All possible neighboring nodes
    adjNodes = [[currRow+1, currCol-1], [currRow+1, currCol], [currRow+1, currCol+1],
                [currRow,   currCol-1],                       [currRow,   currCol+1],
                [currRow-1, currCol-1], [currRow-1, currCol], [currRow-1, currCol+1]]
    
    # Loop through all adjacent nodes, bound check, and add to return lsit if valid
    for adjNode in adjNodes:
        # Bound check
        if adjNode[0] > ybound or adjNode[0] < 0:
            continue
        if adjNode[1] > xbound or adjNode[1] < 0:
            continue
        
        neighbors.append(matrix.getNode(adjNode[0], adjNode[1]))
        
    return neighbors
    
# AStar algorithm
def AStar(matrix, startCords, endCords):
    # Setup starting node
    rootNode = matrix.getNode(startCords[0],startCords[1])
    endNode = matrix.getNode(endCords[0],endCords[1])
    rootNode.parent = rootNode
    rootNode.g = 0
    rootNode.setHuristic(endCords)
    rootNode.f = rootNode.g + rootNode.h
    if doLogging: logmsg("Initalized root node: " + str(rootNode) + "\n")
    
    # Lists to keep track of moves
    openList = [rootNode] # Possible next nodes
    closedList = [] # Nodes already used

    while openList:
        # get cheapest node in openList
        currentNode = sorted(openList, key=lambda node: node.f)[0]
        if doLogging: logmsg("Current Node: " + str(currentNode))
        closedList.append(currentNode)
        openList.remove(currentNode)
        
        # Check if the path has been found
        if currentNode == endNode:
            print("Best path found!")
            parent = currentNode
            path = []
            
            # Construct path
            while parent != rootNode:
                path.append(parent)
                parent = parent.parent
            path.append(rootNode)
            path.reverse()
            
            # Print path
            idx = 1
            for node in path:
                print("({}) ".format(idx) + str(node))
                idx += 1
 
            return True
        
        # get all (bound checked) neighbor nodes of current node
        neighbors = getNeighbors(matrix, currentNode, matrix.rows-1, matrix.cols-1)
        
        if doLogging:
            idx=0
            print("Neighbors:    ",end='')
            for node in neighbors:
                if idx!=0:
                    logmsg("              "+ str(node))
                else:
                    logmsg(str(node))
                idx +=1
            logmsg("")
        
        for node in neighbors:
            # if node == 1: ignore
            if node.value == 1:
                if doLogging: 
                    logmsg("Ignoring: " + str(node))
                    logmsg("Node has value 1\n")
                continue
            
            # if node is in closedList: ignore 
            if node in closedList:
                if doLogging: 
                    logmsg("Ignoring: " + str(node))
                    logmsg("Node is already in closed list\n")
                continue
            
            # if not in openList: update and append
            if node not in openList:
                # make newNode.parent = current node
                node.parent = currentNode
                
                # Update f, g, h
                node.g = node.parent.g + 1
                node.setHuristic(endCords)
                node.f = node.g + node.h
                
                openList.append(node)
                
                if doLogging: logmsg("New node added to openlist: " + str(node))
                continue    
            
            # if in openList
            if node in openList:
                """ If the g value of the currentNode + 1 (for movement) is less than the g value
                of any neighboring nodes, it means that there is a better path and the parent of
                the neight boring node should be set to current node and the values should be recalculated"""
                if currentNode.g + 1 < node.g:
                    oldNode = node
                    node.parent = currentNode
                    node.g = currentNode.g + 1
                    node.f = node.g + node.h
                    
                    if doLogging:
                        logmsg("Better path to neighbor found!: ")
                        logmsg("Old: " + str(oldNode))
                        logmsg("New: " + str(node))
                            
                
        if doLogging: logmsg("-----------------------------------------------------------")
    print("No path found!")

        
        

        
