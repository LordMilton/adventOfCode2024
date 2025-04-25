file = open("input")

for line in file:
    stones = [int(x) for x in line.split(" ")]

PRECOUNTS_LENGTH = 38
TOTAL_BLINKS = 75

preCounts = {}    

def countStones(numBlinks, startStones, usePreCounts=True):
    print("COUNTING STONES")
    print(str(startStones) +" for "+ str(numBlinks) +" blinks")
    preCountedStones = 0
    stones = startStones
    stoneCounts = [len(startStones)]
    for blink in range(0,numBlinks):
        if(blink % 5 == 0):
            print(str(blink) +"/"+ str(numBlinks))
            print("stones list: "+ str(len(stones)))
            print("precounted stones: "+ str(preCountedStones))
        newStones = []
        for stone in stones:
            stoneString = str(stone)
            #Precounts messes up our stored count lists since it only knows endcounts, not intermediate counts
            if(usePreCounts and len(preCounts.get(stone,[]))-1 >= numBlinks-blink):
                preCountedStones += preCounts[stone][numBlinks-blink]
            elif(stone == 0):
                newStones.append(1)
            elif(len(stoneString) % 2 == 0):
                newStones.append(int(stoneString[:int(len(stoneString)/2)]))
                newStones.append(int(stoneString[int(len(stoneString)/2):]))
            else:
                newStones.append(stone*2024)
        stones = newStones
        stoneCounts.append(len(stones))
    stoneCounts[-1] = stoneCounts[-1] + preCountedStones
    return stoneCounts

for x in range(0,10):
    preCounts[x] = countStones(PRECOUNTS_LENGTH, [x], False)

finalStoneCounts = countStones(TOTAL_BLINKS, stones)
print(finalStoneCounts[-1])