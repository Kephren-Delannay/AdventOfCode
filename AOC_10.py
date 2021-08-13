data = []
d= []
with open(file="AOC_10_input.txt") as f:
    d = f.read().split('\n')

for e in d:
    data.append(eval(e))

adapters = data.copy()

#add the outlet
adapters.append(0)


adapters.sort()

#add the device
adapters.append(adapters[-1] + 3)
print(adapters)

ecarts = {1 : 0, 2 : 0, 3: 0}

for i in range(len(adapters) - 1):
    _ec = adapters[i+1] - adapters[i]
    ecarts[_ec] += 1

print(ecarts)
print(ecarts[1] * ecarts[3])