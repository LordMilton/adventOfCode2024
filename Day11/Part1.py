file = open("input")

for line in file:
    stones = [int(x) for x in line.split(" ")]

for blink in range(0,25):
    #print(stones)
    newStones = []
    for stone in stones:
        stoneString = str(stone)
        if(stone == 0):
            newStones.append(1)
        elif(len(stoneString) % 2 == 0):
            newStones.append(int(stoneString[:int(len(stoneString)/2)]))
            newStones.append(int(stoneString[int(len(stoneString)/2):]))
        else:
            newStones.append(stone*2024)
    stones = newStones
print(len(stones))