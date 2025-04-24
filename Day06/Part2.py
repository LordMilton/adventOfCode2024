#Post-mortem: Really should have made something special for the directional symbols and moves
# Had to pass a lot of data that was all interrelated and things get kind of messy

import time
import threading, sys

def printMap(map):
    for row in map:
        for point in row:
            print(point,end=" ")
        print("")
    print("")
    time.sleep(20)
    

file = open("input")
map = []
curCoord = [-1,-1]
curDir = ''
for y,line in enumerate(file):
    map.append(list(line[:-1]))
    if(curCoord[0] < 0):
        if(line.find('^')):
            curCoord = [line.find('^'),y]
            curDir = '^'
        elif(line.find('>')):
            curCoord = [line.find('>'),y]
            curDir = '>'
        elif(line.find('v')):
            curCoord = [line.find('v'),y]
            curDir = 'v'
        elif(line.find('<')):
            curCoord = [line.find('<'),y]
            curDir = '<'
map[curCoord[1]][curCoord[0]] = 'S'
startDir = curDir

# @param map The map
# @param coords Coordinates to start looking for symbolToFind
# @param move Function that shifts the coords in the direction to continue looking
# @param symbolToFind Direction symbol indicating we've moved in this direction in this spot before
# @param altSymbolToFind Direction symbol rotated 90 degrees to the right indicating we've been on this path before (only relevant if there's an obstacle right after it, see diagram)
# ..#.....
# >>>>>>>#
# ..^...v.
# <O<<<<<.
# ......#.
def couldLoop(map, coords, move, symbolToFind, altSymbolToFind):
    curCoords = coords
    curSymbol = map[coords[1]][coords[0]]
    while(inBounds(map, curCoords) and curSymbol != '#'):
        curSymbol = map[curCoords[1]][curCoords[0]]
        if(curSymbol == symbolToFind):
            return True
        nextCoords = move(curCoords)
        if(inBounds(map, nextCoords)):
            nextSymbol = map[nextCoords[1]][nextCoords[0]]
            # In the case of an obstacle that's never caused us to turn, but crashing into it and turning would put us on a previously used path
            if(nextSymbol == '#' and curSymbol == altSymbolToFind):
                return True
        curCoords = move(curCoords)
    return False

def getNextSymbol(symbol):
    if(symbol == '^'):
        return '>'
    if(symbol == '>'):
        return 'v'
    if(symbol == 'v'):
        return '<'
    if(symbol == '<'):
        return '^'

upMove = lambda coords : [coords[0], coords[1]-1]
rightMove = lambda coords : [coords[0]+1, coords[1]]
downMove = lambda coords : [coords[0], coords[1]+1]
leftMove = lambda coords : [coords[0]-1, coords[1]]
def getMoveForSymbol(symbol):
    if(symbol == '^'):
        return upMove
    if(symbol == '>'):
        return rightMove
    if(symbol == 'v'):
        return downMove
    if(symbol == '<'):
        return leftMove
    
def getMapSymbol(map, coords):
    return map[coords[1]][coords[0]]
        
def inBounds(map, coords):
    return(not(coords[0] < 0 or coords[0] >= len(map[0]) or coords[1] < 0 or coords[1] >= len(map)))

def strcon(string, substring):
    return(string.find(substring) >= 0)

def run(map, curCoord, curDir, startDir, obstacleAlreadyPlaced=False, obstaclesPlaced=0, recursionDepth = 0):
    #printMap(map)
    if(obstacleAlreadyPlaced and strcon(map[curCoord[1]][curCoord[0]],curDir)):
        #printMap(map)
        print("uniqueObstacle Found")
        return obstaclesPlaced + 1
    curSpot = map[curCoord[1]][curCoord[0]]
    nextCoord = getMoveForSymbol(curDir)(curCoord)
    if(not inBounds(map, nextCoord)):
        if(obstacleAlreadyPlaced):
            map[curCoord[1]][curCoord[0]] = curSpot
        return obstaclesPlaced
    nextSpot = map[nextCoord[1]][nextCoord[0]]
    if(not obstacleAlreadyPlaced):
        nextNextCoord = getMoveForSymbol(curDir)(nextCoord)
        nextNextSpot = 'S'
        if(inBounds(map, nextNextCoord)):
            nextNextSpot = map[nextNextCoord[1]][nextNextCoord[0]]
        if(not strcon(nextNextSpot,'S') and not strcon(nextNextSpot,'#') and not strcon(nextSpot,'#') and not strcon(nextNextSpot,'1')):
            map[nextNextCoord[1]][nextNextCoord[0]] = map[nextNextCoord[1]][nextNextCoord[0]] + '0'
            obstaclesPlaced = run(map, nextCoord, getNextSymbol(curDir), startDir, obstacleAlreadyPlaced=True, obstaclesPlaced=obstaclesPlaced, recursionDepth = recursionDepth+1)
            map[nextNextCoord[1]][nextNextCoord[0]] = nextNextSpot +'1'
    nextDir = curDir
    if(strcon(nextSpot,'#') or strcon(nextSpot,'0')):
        nextDir = getNextSymbol(curDir)
        nextCoord = curCoord
    #printMap(map)
    
    map[curCoord[1]][curCoord[0]] = map[curCoord[1]][curCoord[0]] + curDir
    newObstaclesPlaced = run(map, nextCoord, nextDir, startDir, obstacleAlreadyPlaced=obstacleAlreadyPlaced, obstaclesPlaced=obstaclesPlaced, recursionDepth = recursionDepth+1)
    if(obstacleAlreadyPlaced):
        map[curCoord[1]][curCoord[0]] = curSpot
    return(newObstaclesPlaced)
    
def main():
    uniqueObstacles = 0
    for y,row in enumerate(map):
        for x,spot in enumerate(row):
            if(not strcon(spot,'S') and not strcon(spot, '#')):
                map[y][x] = spot + "0"
                uniqueObstacles += run(map, curCoord, curDir, startDir, True)
                map[y][x] = spot
                
    print(uniqueObstacles)
    
sys.setrecursionlimit(300000)
threading.stack_size(2**27)
threading.Thread(target=main).start()
    
"""
    if(curDir == '^'):
        curSpot = map[curCoord[1]][curCoord[0]]
        nextCoord = upMove(curCoord)
        if(not inBounds(map, nextCoord)):
            return obstaclesPlaced
        nextSpot = map[nextCoord[1]][nextCoord[0]]
        if(nextSpot == 'S'):
            nextSpot = startDir
        if(not obstacleAlreadyPlaced):
            nextNextCoord = upMove(nextCoord)
            nextNextSpot = 'S'
            if(inBounds(map, nextNextCoord)):
                nextNextSpot = map[nextNextCoord[1]][nextNextCoord[0]]
            if(nextNextSpot != 'S'):
                map[nextNextCoord[1]][nextNextCoord[0]] = '0'
                obstaclesPlaced = run(map, nextCoord, '>', startDir, obstacleAlreadyPlaced=True, obstaclesPlaced=obstaclesPlaced)
                map[nextNextCoord[1]][nextNextCoord[0]] = nextNextSpot
        nextDir = curDir
        if(nextSpot == '#'):
            nextDir = '>'
            nextCoord = curCoord
        printMap(map)
        newObstaclesPlaced = run(map, nextCoord, nextDir, startDir, obstaclesPlaced=obstaclesPlaced)
        if(obstacleAlreadyPlaced):
            map[curCoord[1]][curCoord[0]] = curSpot
        return(newObstaclesPlaced)
    elif(curDir == '>'):
        curSpot = map[curCoord[1]][curCoord[0]]
        nextCoord = rightMove(curCoord)
        if(not inBounds(map, nextCoord)):
            return obstaclesPlaced
        nextSpot = map[nextCoord[1]][nextCoord[0]]
        if(nextSpot == 'S'):
            nextSpot = startDir
        if(not obstacleAlreadyPlaced):
            nextNextCoord = rightMove(nextCoord)
            nextNextSpot = 'S'
            if(inBounds(map, nextNextCoord)):
                nextNextSpot = map[nextNextCoord[1]][nextNextCoord[0]]
            if(nextNextSpot != 'S'):
                obstaclesPlaced = run(map, nextCoord, 'v', startDir, obstacleAlreadyPlaced=True, obstaclesPlaced=obstaclesPlaced)
        nextDir = curDir
        if(nextSpot == '#'):
            nextDir = 'v'
            nextCoord = curCoord
        printMap(map)
        newObstaclesPlaced = run(map, nextCoord, nextDir, startDir, obstaclesPlaced=obstaclesPlaced)
        if(obstacleAlreadyPlaced):
            map[curCoord[1]][curCoord[0]] = curSpot
        return(newObstaclesPlaced)
    elif(curDir == 'v'):
        curSpot = map[curCoord[1]][curCoord[0]]
        nextCoord = downMove(curCoord)
        if(not inBounds(map, nextCoord)):
            return obstaclesPlaced
        nextSpot = map[nextCoord[1]][nextCoord[0]]
        if(nextSpot == 'S'):
            nextSpot = startDir
        if(not obstacleAlreadyPlaced):
            nextNextCoord = downMove(nextCoord)
            nextNextSpot = 'S'
            if(inBounds(map, nextNextCoord)):
                nextNextSpot = map[nextNextCoord[1]][nextNextCoord[0]]
            if(nextNextSpot != 'S'):
                obstaclesPlaced = run(map, nextCoord, '<', startDir, obstacleAlreadyPlaced=True, obstaclesPlaced=obstaclesPlaced)
        nextDir = curDir
        if(nextSpot == '#'):
            nextDir = '<'
            nextCoord = curCoord
        printMap(map)
        newObstaclesPlaced = run(map, nextCoord, nextDir, startDir, obstaclesPlaced=obstaclesPlaced)
        if(obstacleAlreadyPlaced):
            map[curCoord[1]][curCoord[0]] = curSpot
        return(newObstaclesPlaced)
    elif(curDir == '<'):
        curSpot = map[curCoord[1]][curCoord[0]]
        nextCoord = leftMove(curCoord)
        if(not inBounds(map, nextCoord)):
            return obstaclesPlaced
        nextSpot = map[nextCoord[1]][nextCoord[0]]
        if(nextSpot == 'S'):
            nextSpot = startDir
        if(not obstacleAlreadyPlaced):
            nextNextCoord = leftMove(nextCoord)
            nextNextSpot = 'S'
            if(inBounds(map, nextNextCoord)):
                nextNextSpot = map[nextNextCoord[1]][nextNextCoord[0]]
            if(nextNextSpot != 'S'):
                obstaclesPlaced = run(map, nextCoord, '^', startDir, obstacleAlreadyPlaced=True, obstaclesPlaced=obstaclesPlaced)
        nextDir = curDir
        if(nextSpot == '#'):
            nextDir = '^'
            nextCoord = curCoord
        printMap(map)
        newObstaclesPlaced = run(map, nextCoord, nextDir, startDir, obstaclesPlaced=obstaclesPlaced)
        if(obstacleAlreadyPlaced):
            map[curCoord[1]][curCoord[0]] = curSpot
        return(newObstaclesPlaced)
"""
    
"""
    if(map[curCoord[1]][curCoord[0]] != 'S'):
        map[curCoord[1]][curCoord[0]] = curDir
    
    if(curDir == '^'):
        curSpot = map[curCoord[1]][curCoord[0]]
        nextCoord = upMove(curCoord)
        if(not inBounds(map, nextCoord)):
            break
        nextSpot = map[nextCoord[1]][nextCoord[0]]
        if(nextSpot == 'S'):
            nextSpot = startDir
        nextNextCoord = upMove(nextCoord)
        nextNextSpot = 'S'
        if(inBounds(map, nextNextCoord)):
            nextNextSpot = map[nextNextCoord[1]][nextNextCoord[0]]
            
        if(nextNextSpot != 'S' and couldLoop(map, nextCoord, rightMove, '>', 'v')):
            obstacleSpots += 1
        if(nextSpot == '#'):
            curDir = '>'
        else:
            curCoord = nextCoord
    elif(curDir == '>'):
        curSpot = map[curCoord[1]][curCoord[0]]
        nextCoord = rightMove(curCoord)
        if(not inBounds(map, nextCoord)):
            break
        nextSpot = map[nextCoord[1]][nextCoord[0]]
        if(nextSpot == 'S'):
            nextSpot = startDir
        nextNextCoord = rightMove(nextCoord)
        nextNextSpot = 'S'
        if(inBounds(map, nextNextCoord)):
            nextNextSpot = map[nextNextCoord[1]][nextNextCoord[0]]
            
        if(nextNextSpot != 'S' and couldLoop(map, nextCoord, downMove, 'v', '<')):
            obstacleSpots += 1
        if(nextSpot == '#'):
            curDir = 'v'
        else:
            curCoord = nextCoord
    elif(curDir == 'v'):
        curSpot = map[curCoord[1]][curCoord[0]]
        nextCoord = downMove(curCoord)
        if(not inBounds(map, nextCoord)):
            break
        nextSpot = map[nextCoord[1]][nextCoord[0]]
        if(nextSpot == 'S'):
            nextSpot = startDir
        nextNextCoord = downMove(nextCoord)
        nextNextSpot = 'S'
        if(inBounds(map, nextNextCoord)):
            nextNextSpot = map[nextNextCoord[1]][nextNextCoord[0]]
            
        if(nextNextSpot != 'S' and couldLoop(map, nextCoord, leftMove, '<', '^')):
            obstacleSpots += 1
        if(nextSpot == '#'):
            curDir = '<'
        else:
            curCoord = nextCoord
    elif(curDir == '<'):
        curSpot = map[curCoord[1]][curCoord[0]]
        nextCoord = leftMove(curCoord)
        if(not inBounds(map, nextCoord)):
            break
        nextSpot = map[nextCoord[1]][nextCoord[0]]
        if(nextSpot == 'S'):
            nextSpot = startDir
        nextNextCoord = leftMove(nextCoord)
        nextNextSpot = 'S'
        if(inBounds(map, nextNextCoord)):
            nextNextSpot = map[nextNextCoord[1]][nextNextCoord[0]]
            
        if(nextNextSpot != 'S' and couldLoop(map, nextCoord, upMove, '^', '>')):
            obstacleSpots += 1
        if(nextSpot == '#'):
            curDir = '^'
        else:
            curCoord = nextCoord
"""