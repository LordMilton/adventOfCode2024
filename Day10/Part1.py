import copy
import queue

file = open("input")

map = []
trailheads = []
for lineNum,line in enumerate(file):
    map.append([int(x) for x in line[:-1]])
    trailheads.extend([[lineNum,enum] for enum,x in enumerate(line) if x == '0'])

def getMapValueAt(map, position):
    return map[position[0]][position[1]]

movements = [lambda coord : [coord[0]+1,coord[1]], lambda coord : [coord[0]-1,coord[1]], lambda coord : [coord[0],coord[1]+1], lambda coord : [coord[0],coord[1]-1]]
trailheadScore = 0
for trailhead in trailheads:
    tempMap = copy.deepcopy(map)
    possiblePositions = queue.Queue()
    possiblePositions.put(trailhead)
    while not possiblePositions.empty():
        curPos = possiblePositions.get()
        print(curPos)
        if(getMapValueAt(tempMap, curPos) == 9):
            trailheadScore += 1
            tempMap[curPos[0]][curPos[1]] = 11 #Make it unreachable so we won't double count it
        for operation in movements:
            nextPos = operation(curPos)
            if(nextPos[0] >= 0 and nextPos[0] < len(map) and nextPos[1] >= 0 and nextPos[1] < len(map[0]) and
                getMapValueAt(tempMap, nextPos) - getMapValueAt(tempMap, curPos) == 1):
                possiblePositions.put(nextPos)
        tempMap[curPos[0]][curPos[1]] = 11
                

print(trailheadScore)    