import re

def doMul(function):
    nums = [int(x) for x in re.findall("\d{1,3}", function)]
    return(nums[0] * nums[1])

file = open("input")
total = 0
for line in file:
    muls = re.findall("mul\(\d{1,3},\d{1,3}\)", line)
    total += sum([doMul(mul) for mul in muls])
    
print(total)