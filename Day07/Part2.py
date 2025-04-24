file = open("input")
equations = []
for line in file:
    equation = []
    split = line.split(":")
    equation.append(int(split[0]))
    split = split[1][1:-1].split(" ")
    equation.append([int(x) for x in split])
    equations.append(equation)
print(equations)

def testOpsRec(nums, goal):
    if(len(nums) == 1):
        return(nums[0] == goal)
    else:
        numsAdd = [nums[0] + nums[1]]
        numsAdd.extend(nums[2:])
        numsMul = [nums[0] * nums[1]]
        numsMul.extend(nums[2:])
        numsOr = [int(str(nums[0]) + str(nums[1]))]
        numsOr.extend(nums[2:])
        return(testOpsRec(numsAdd, goal) or
               testOpsRec(numsMul, goal) or
               testOpsRec(numsOr, goal))
        
total = 0
for equation in equations:
    if(testOpsRec(equation[1], equation[0])):
        total += equation[0]
        
print(total)