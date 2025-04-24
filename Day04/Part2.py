def findXmas(letters, xPos, yPos):
    xmasCount = 0
    if(letters[yPos][xPos] == "A"):
        if(isXmas(letters, xPos, yPos)):
            xmasCount += 1
    return xmasCount

def isXmas(letters, xPos, yPos):
    if(xPos-1 < 0 or xPos+1 >= len(letters[0]) or
       yPos-1 < 0 or yPos+1 >= len(letters)):
        return False
    word1 = ""
    word2 = ""
    for z in range(-1,2):
        word1 += letters[yPos+(z)][xPos+(z)]
        word2 += letters[yPos-(z)][xPos+(z)]
    return ((word1 == "SAM" or word1 == "MAS") and (word2 == "SAM" or word2 == "MAS"))

file = open("input")

letters = []
for line in file:
    letters.append(line[:-1])

totalXmas = 0
for y,line in enumerate(letters):
    for x,letter in enumerate(line):
        totalXmas += findXmas(letters, x, y)
        
print(totalXmas)
