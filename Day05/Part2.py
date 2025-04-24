import math

file = open("input")
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
print(rules)

# This directly affects the page sort function and needs to be changed per book before using said sort
curPageHier = []

# Make page hierarchy
def makePageHier(rules, book):
    tempRules = {}
    for page in book:
        tempRules[page] = rules.get(page,[])
    pageHier = []
    while len(tempRules) > 0:
        curPageNumNextInHier = False
        precedents = tempRules.keys()
        #print(precedents)
        curPageNum = 0
        for precedent in precedents:
            curPageNum = precedent
            break
        while(not curPageNumNextInHier):
            #print("cur"+ str(curPageNum))
            curPageNumNextInHier = True
            for precedentPageNum in precedents:
                #print(precedentPageNum)
                # if the current precedent is the current page number's precedent
                if(precedentPageNum != curPageNum and tempRules.get(precedentPageNum).count(curPageNum) > 0):
                    curPageNum = precedentPageNum
                    #print(tempRules.get(precedentPageNum))
                    curPageNumNextInHier = False
                    break
        pageHier.append(curPageNum)
        #print(pageHier)
        tempRules.pop(curPageNum)
    print(pageHier)
    return pageHier

def pageSortFun(page):
    index = 10000000
    try:
        index = curPageHier.index(page)
    except:
        pass
    return index

middlePages = []
for book in books:
    previous = {}
    fails = False
    for page in book:
        previous[page] = True
        for rule in rules.get(page,[]):
            fails = fails or previous.get(rule, False)
    if(fails):
        print("book: "+ str(book) +" fails")
        curPageHier = makePageHier(rules, book)
        book.sort(key=pageSortFun)
        print("sortedBook=" +str(book))
        middlePages.append(book[math.floor(len(book)/2)])
    else:
        print("book: "+ str(book) +" succeeds")

print(sum(middlePages))
