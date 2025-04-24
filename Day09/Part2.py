file = open("input")
input = file.readline()
input = input[:len(input)-1]

blockNum = 0
memory = []
blankLenDir = {}
largestBlank = 0
memoryLenDir = {}
memoryDir = {}
blank = False
for char in input:
    length = int(char)
    if(not blank):
        memoryDir[str(blockNum)] = len(memory)
        memoryLenDir[str(blockNum)] = length
        memory.extend([str(blockNum)]*length)
        blockNum += 1
    else:
        newBlankSect = blankLenDir.get(length,[])
        newBlankSect.append(len(memory))
        largestBlank = max(largestBlank, length)
        blankLenDir[length] = newBlankSect
        memory.extend(["."]*length)
    blank = not blank
endVal = memory[-1]
while endVal == '.':
    memory.pop[-1]
    endVal = memory[-1]
print(blankLenDir)
print(memoryDir)
print(memoryLenDir)
print(largestBlank)

def getLeftmostBlockOfLengthOrGreater(minLength, maxIndex):
    #print("looking for blank space at least "+ str(minLength) +" large")
    curLength = minLength
    leftMostBlock = len(memory)
    leftMostBlockLen = 0
    while curLength <= largestBlank:
        if(len(blankLenDir.get(curLength, [])) > 0 and leftMostBlock > (blankLenDir.get(curLength, [len(memory)])[0])):
            leftMostBlock = blankLenDir[curLength][0]
            leftMostBlockLen = curLength
        #print("might be at index "+ str(leftMostBlock) +" and of length "+ str(leftMostBlockLen))
        curLength += 1
    if(leftMostBlock > maxIndex): #If we would be moving the fileID to the right
        leftMostBlockLen = 0
    return([leftMostBlock, leftMostBlockLen])

def memoryCleanup(leftBlockStartIndex, originalBlankBlockLength, rightBlockStartIndex, blockLength):
    # Add new, smaller blank to appropriate place in directory
    newSmallerBlankDir = blankLenDir.get(originalBlankBlockLength-length,[])
    newSmallerBlankDir.append(leftBlockStartIndex+length)
    blankLenDir[originalBlankBlockLength-length] = newSmallerBlankDir
    blankLenDir[originalBlankBlockLength-length].sort()
    # Remove original blank from directory
    blankLenDir[originalBlankBlockLength] = blankLenDir[originalBlankBlockLength][1:]
    # Combine new blank in place of fileIDs with surrounding blanks and add to directory
    # This is irrelevant since we only move right to left, space freed by moving fileIDs will have no chance to be used
    
curBlockNum = blockNum-1
while curBlockNum >= 0:
    if(curBlockNum % 100 == 0):
        print(curBlockNum)
    length = memoryLenDir[str(curBlockNum)]
    leftMostBlockInfo = getLeftmostBlockOfLengthOrGreater(length, memoryDir[str(curBlockNum)])
    leftMostBlockIndex = leftMostBlockInfo[0]
    leftMostBlockLength = leftMostBlockInfo[1]
    curBlockNumIndex = memoryDir[str(curBlockNum)]
    if(leftMostBlockLength > 0):
        print("altered")
        modifiedMemory = memory[0:leftMostBlockIndex] #Start of memory unchanged
        modifiedMemory.extend([str(curBlockNum)]*length) #Copy fileID into empty space
        modifiedMemory.extend(memory[leftMostBlockIndex+length:curBlockNumIndex]) #memory between fileID's new and original space unchanged
        modifiedMemory.extend(["."]*length) #Copy blank space into fileID's original space
        modifiedMemory.extend(memory[curBlockNumIndex+length:]) #End of memory unchanged
        #print(modifiedMemory)
        memory = modifiedMemory
        memoryCleanup(leftMostBlockIndex, leftMostBlockLength, curBlockNumIndex, length)
    else:
        print("unchanged")
    
    curBlockNum -= 1
    
print(memory)

def intifyValue(x):
    if(x == "."):
        return(0)
    return(int(x))
checksum = 0
for mul,num in enumerate([intifyValue(x) for x in memory]):
    checksum += mul*num

print(checksum)