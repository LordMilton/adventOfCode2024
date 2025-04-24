import time

def printMap(map):
    for row in map:
        for point in row:
            #time.sleep(.5)
            print(point,end="")
        print("")
    print("")

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
printMap(map)

uniqueSpots = 0
while(True):
    if(map[curCoord[1]][curCoord[0]] != 'X'):
        uniqueSpots += 1
    map[curCoord[1]][curCoord[0]] = 'X'
    
    if(curDir == '^'):
        curSpot = map[curCoord[1]][curCoord[0]]
        nextCoord = [curCoord[0], curCoord[1]-1]
        if(nextCoord[1] < 0):
            break
        nextSpot = map[nextCoord[1]][nextCoord[0]]
        if(nextSpot == '#'):
            curDir = '>'
        else:
            curCoord = nextCoord
    elif(curDir == '>'):
        curSpot = map[curCoord[1]][curCoord[0]]
        nextCoord = [curCoord[0]+1, curCoord[1]]
        if(nextCoord[0] >= len(map[0])):
            break
        nextSpot = map[nextCoord[1]][nextCoord[0]]
        if(nextSpot == '#'):
            curDir = 'v'
        else:
            curCoord = nextCoord
    elif(curDir == 'v'):
        curSpot = map[curCoord[1]][curCoord[0]]
        nextCoord = [curCoord[0], curCoord[1]+1]
        if(nextCoord[1] >= len(map)):
            break
        nextSpot = map[nextCoord[1]][nextCoord[0]]
        if(nextSpot == '#'):
            curDir = '<'
        else:
            curCoord = nextCoord
    elif(curDir == '<'):
        curSpot = map[curCoord[1]][curCoord[0]]
        nextCoord = [curCoord[0]-1, curCoord[1]]
        if(nextCoord[0] < 0):
            break
        nextSpot = map[nextCoord[1]][nextCoord[0]]
        if(nextSpot == '#'):
            curDir = '^'
        else:
            curCoord = nextCoord
            
printMap(map)
print(uniqueSpots)