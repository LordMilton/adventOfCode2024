input = open('input')
listA = []
bCount = dict()
for line in input:
    splitline = line.split()
    listA.append(splitline[0])
    bCount[splitline[1]] = bCount.get(splitline[1], 0) + 1

print(listA)
print(bCount)

similarity = 0
for intA in listA:
    similarity += int(intA) * bCount.get(intA, 0)

print(similarity)
