with open(file="AOC_9_input.txt") as f:
    data = f.read().split('\n')

target = 400480901
test_data=['35',
'20',
'15',
'25',
'47',
'40',
'62',
'55',
'65',
'95',
'102',
'117',
'150',
'182',
'127',
'219',
'299',
'277',
'309',
'576']

s = eval(data[0])
startindex = 0
l = []
i = 1

l.append(eval(data[startindex]))
while s != target and i < len(data) :
    s += eval(data[startindex + i])
    print(s)
    l.append(eval(data[startindex + i]))
    print(l)
    while s > target:
        #! MODIFY TO WHILE S > TARGET
        print("------------------------")
        s -= l[0]
        l.pop(0)
        print(l)
    i += 1
print(s)
l.sort()
print(l[0] + l[-1])
print(sum(l))
