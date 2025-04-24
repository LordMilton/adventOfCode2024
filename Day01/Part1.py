input = open('input')
listA = []
listB = []
for line in input:
    splitline = line.split()
    listA.append(splitline[0])
    listB.append(splitline[1])

listA.sort()
print(listA)
listB.sort()
print(listB)
difference = 0
for (intA, intB) in zip(listA, listB):
    difference += abs(int(intA) - int(intB))

print(difference)
