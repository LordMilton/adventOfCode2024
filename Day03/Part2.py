import re

def doMul(function):
    nums = [int(x) for x in re.findall("\d{1,3}", function)]
    print(nums)
    return(nums[0] * nums[1])

file = open("input")
input = ""
for line in file:
    input += line[:-1]
    
print(input)
insts = re.findall("^(?:.(?!don't\(\)))*.don't\(\)" + "|do\(\)(?:.(?!don't\(\)))*.don't\(\)" + "|do\(\)(?:.(?!don't\(\)))*$", input)
print(insts)
muls = [re.findall("mul\(\d{1,3},\d{1,3}\)", instStr) for instStr in insts]
mulsFlattened = [x for row in muls for x in row]
print(mulsFlattened)
total = sum([doMul(mul) for mul in mulsFlattened])

print(total)