with open(file='AOC_2_input.txt') as f:
    data = f.readlines()

"""
def check_valid(combin):
    processed = combin.split(" ")
    counts = processed[0].split("-")
    count_min = int(counts[0])
    count_max = int(counts[1])
    check = processed[1][0]
    password = str(combin.split(":")[1])
    #print(count_min, count_max,check, password)
    return password.count(check) >= count_min and password.count(check) <= count_max

#print(check_valid(data[-1]))
#print((data[-1]))

total = 0
for combination in data:
    if check_valid(combination):
        total += 1
print(total)"""

def newcheck(combin):
    processed = combin.split(" ")
    poses = processed[0].split("-")
    pos1 = int(poses[0])
    pos2 = int(poses[1])
    check = processed[1][0]
    password = str(combin.split(":")[1]).replace(" ", "")
    return (password[pos1-1] == check and password[pos2-1] != check) or (password[pos1-1] != check and password[pos2-1] == check)

total = 0
for combination in data:
    if newcheck(combination):
        total += 1
print(total)

"""print(data[968])
print(newcheck((data[968])))
print((data[968][3] == "m" and data[968][9] != "m") or (data[968][3] != "m" and data[968][9] == "m"))"""