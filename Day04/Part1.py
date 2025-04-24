def findXmas(letters, xPos, yPos):
    xmasCount = 0
    if(letters[yPos][xPos] == "X"):
        for dx in range(-1,2):
            for dy in range(-1,2):
                if(isXmas(letters, xPos, yPos, dx, dy)):
                    print("CHRISTMAS")
                    xmasCount += 1
    return xmasCount

def isXmas(letters, xPos, yPos, dx, dy):
    if(xPos+(dx*3) < 0 or xPos+(dx*3) >= len(letters[0]) or
       yPos+(dy*3) < 0 or yPos+(dy*3) >= len(letters)):
        return False
    word = ""
    for z in range(0,4):
        word += letters[yPos+(dy*z)][xPos+(dx*z)]
    return (word == "XMAS")

file = open("input")

letters = []
for line in file:
    letters.append(line[:-1])
print(letters)

totalXmas = 0
for y,line in enumerate(letters):
    for x,letter in enumerate(line):
        totalXmas += findXmas(letters, x, y)
        
print(totalXmas)
