
import math
file = open("sampleinput")
section = 1
rules = {}
books = []
for line in file:
    if(section == 1):
        split = line.split("|")
        if(len(split) < 2):
            section += 1
        else:
            split = [int(page) for page in split]
            currentRules = rules.get(split[0], [])
            currentRules.append(split[1])
            rules[split[0]] = currentRules
    elif(section == 2):
        books.append([int(page) for page in line.split(",")])

middlePages = []
for book in books:
    previous = {}
    fails = False
    for page in book:
        previous[page] = True
        for rule in rules.get(page,[]):
            fails = fails or previous.get(rule, False)
    if(not fails):
        middlePages.append(book[math.floor(len(book)/2)])

print(sum(middlePages))