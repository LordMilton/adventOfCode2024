file = open("sampleinput")
input = file.readline()
input = input[:len(input)-1]

blockNum = 0
memory = []
blank = False
for char in input:
    length = int(char)
    if(not blank):
        memory.extend([str(blockNum)]*length)
        blockNum += 1
    else:
        memory.extend(["."]*length)
    blank = not blank
endVal = memory[-1]
while endVal == '.':
    memory.pop[-1]
    endVal = memory[-1]

beginningMark = memory.index(".")
endingMark = len(memory)-1
while endingMark > beginningMark:
    memory[beginningMark] = memory[endingMark]
    memory.pop(-1)
    endingMark -= 1
    beginningMark += 1
    while memory[beginningMark] != '.' and beginningMark < len(memory)-1:
        beginningMark += 1
    while memory[endingMark] == '.':
        memory.pop(-1)
        endingMark -= 1
print(memory)

checksum = 0
for mul,num in enumerate([int(x) for x in memory]):
    checksum += mul*num

print(checksum)