"""with open(file="AOC_3_input.txt") as f:
    data = f.readlines()

height = 0
curx = 0
num = 0

while height < len(data) - 1:
    nextx = ((curx + 3)%31) 
    nextpos = data[height + 1][nextx]
    if nextpos == "#": 
        num += 1
    height += 1
    curx = nextx
print("height : " + str(height))
print("num : " + str(num))"""

import functools

with open(file="AOC_3_input.txt") as f:
    data = f.readlines()


results = []

def checkslope(slopex, slopey):
    height = 0
    curx = 0
    num = 0
    while height < len(data) - slopey:
        nextx = ((curx + slopex)%31) 
        nextpos = data[height + slopey][nextx]
        if nextpos == "#": 
            num += 1
        height += slopey
        curx = nextx
    return num

#slope 1 
n1 = checkslope(1,1)
print("num1 : " + str(n1))
results.append(n1)

#slope 2
n1 = checkslope(3,1)
print("num2 : " + str(n1))
results.append(n1)

#slope 3
n1 = checkslope(5,1)
print("num3 : " + str(n1))
results.append(n1)

#slope 4
n1 = checkslope(7,1)
print("num4 : " + str(n1))
results.append(n1)

#slope 5
n1 = checkslope(1,2)
print("num5 : " + str(n1))
results.append(n1)

print(functools.reduce(lambda x,y : x * y, results))