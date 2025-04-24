# < 217
file = open("input")

xBound = 0
yBound = 0
antennaeLocs = {}
for y,line in enumerate(file):
    yBound += 1
    # -1 to discount \n at the end of the lines
    xBound = len(line)-1
    for x,char in enumerate(line[0:len(line)-1]):
        if(char != '.'):
            temp = antennaeLocs.get(char, [])
            temp.append([x,y])
            antennaeLocs[char] = temp
print(xBound)
print(yBound)

def isWithinBound(coords):
    return(0 <= coords[1] < xBound and 0 <= coords[0] < yBound)

def areWhole(coords):
    return(coords[1] == int(coords[1]) and coords[0] == int(coords[0]))

def addIfValid(aNodes, coords):
    if(isWithinBound(coords) and areWhole(coords)):
        addIfUnique(aNodes, [int(coords[0]), int(coords[1])])
    return aNodes

def addIfUnique(aNodes, coords):
    for aNode in aNodes:
        if(aNode[0] == coords[0] and aNode[1] == coords[1]):
            return aNodes
    aNodes.append(coords)
    #print(coords)
    return aNodes

aNodes = []
for antennaType in antennaeLocs.keys():
    for antennaNum,loc in enumerate(antennaeLocs[antennaType]):
        for loc2 in antennaeLocs[antennaType][antennaNum+1:]:
            yDistance = loc[0] - loc2[0]
            xDistance = loc[1] - loc2[1]
            print("aNodes: "+ str(loc) + str(loc2))
            potentialANodes = []
            # #..A..A...
            potentialANodes.append([loc[0]+yDistance, loc[1]+xDistance])
            # ...A..A..#
            potentialANodes.append([loc2[0]-yDistance, loc2[1]-xDistance])
            # ...A#.A...
            #potentialANodes.append([loc[0]-(yDistance/3), loc[1]-(xDistance/3)])
            # ...A.#A...
            #potentialANodes.append([loc2[0]+(yDistance/3), loc2[1]+(xDistance/3)])
            for aNode in potentialANodes:
                #print(aNode)
                addIfValid(aNodes, aNode)
print(aNodes)
print(len(aNodes))
            